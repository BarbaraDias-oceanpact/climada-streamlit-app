import folium
from folium.plugins import HeatMap
import tkinter as tk
from tkinter import filedialog
import webbrowser
from climada_integration import *  # Importa as funções do Passo 3

class RiskApp:
    def __init__(self, root):
        self.root = root
        self.setup_ui()
        
    def setup_ui(self):
        # Configuração da janela
        self.root.title("CLIMADA - Análise de Risco para Embarcações")
        
        # Widgets
        tk.Label(self.root, text="Arquivo NetCDF:").pack()
        self.netcdf_entry = tk.Entry(self.root, width=50)
        self.netcdf_entry.pack()
        tk.Button(self.root, text="Procurar", command=self.browse_netcdf).pack()
        
        tk.Label(self.root, text="Arquivo CSV de Embarcações:").pack()
        self.csv_entry = tk.Entry(self.root, width=50)
        self.csv_entry.pack()
        tk.Button(self.root, text="Procurar", command=self.browse_csv).pack()
        
        tk.Label(self.root, text="Limite de Risco (m para ondas):").pack()
        self.threshold_entry = tk.Entry(self.root)
        self.threshold_entry.insert(0, "2.0")  # Valor padrão
        self.threshold_entry.pack()
        
        tk.Button(self.root, text="Gerar Mapa de Risco", command=self.run_analysis).pack()
        
    def browse_netcdf(self):
        filename = filedialog.askopenfilename(filetypes=[("NetCDF Files", "*.nc")])
        self.netcdf_entry.delete(0, tk.END)
        self.netcdf_entry.insert(0, filename)
    
    def browse_csv(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        self.csv_entry.delete(0, tk.END)
        self.csv_entry.insert(0, filename)
    
    def run_analysis(self):
        # Carrega dados
        ocean_data = load_ocean_data(self.netcdf_entry.get())
        vessels = load_vessels(self.csv_entry.get())
        threshold = float(self.threshold_entry.get())
        
        # Processamento
        hazard = create_hazard_map(ocean_data, threshold)
        impact = calculate_impact(hazard, vessels)
        cost_df = generate_cost_analysis(impact, daily_rate=5000)  # Taxa diária de exemplo
        
        # Mapa Folium
        m = folium.Map(
            location=[-23.5, -45.0],  # Centro na Bacia de Santos
            zoom_start=7,
            tiles="cartodbpositron"
        )
        
        # Hotspots de risco
        HeatMap(
            data=ocean_data[['lat', 'lon', 'wave_height']].values,
            radius=15,
            blur=10
        ).add_to(m)
        
        # Embarcações afetadas
        for _, row in vessels.gdf.iterrows():
            folium.CircleMarker(
                location=[row.geometry.y, row.geometry.x],
                radius=5,
                color='red' if row['id'] in cost_df[cost_df['downtime_days'] > 0]['vessel_id'] else 'green',
                fill=True,
                popup=f"Embarcação {row['id']} - Custo: ${cost_df[cost_df['vessel_id'] == row['id']]['total_cost'].values[0]:.2f}"
            ).add_to(m)
        
        # Salva e abre o mapa
        m.save("output/risk_map.html")
        webbrowser.open("output/risk_map.html")

if __name__ == "__main__":
    root = tk.Tk()
    app = RiskApp(root)
    root.mainloop()
