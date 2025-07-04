import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import webbrowser
from modules.climada_analysis import load_netcdf_data, calculate_impact
from modules.cost_calculator import calculate_losses
from modules.folium_map import create_risk_map

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CLIMADA - Análise de Risco para Embarcações")
        
        # Variáveis de entrada
        self.netcdf_path = tk.StringVar()
        self.csv_path = tk.StringVar()
        self.wave_threshold = tk.DoubleVar(value=2.0)  # Padrão: 2m de onda
        
        # Widgets
        ttk.Label(self.root, text="Arquivo NetCDF:").pack()
        ttk.Entry(self.root, textvariable=self.netcdf_path).pack()
        ttk.Button(self.root, text="Selecionar", command=self.browse_netcdf).pack()
        
        ttk.Label(self.root, text="CSV de Embarcações:").pack()
        ttk.Entry(self.root, textvariable=self.csv_path).pack()
        ttk.Button(self.root, text="Selecionar", command=self.browse_csv).pack()
        
        ttk.Label(self.root, text="Altura de Onda Limite (m):").pack()
        ttk.Entry(self.root, textvariable=self.wave_threshold).pack()
        
        ttk.Button(self.root, text="Calcular Risco e Custos", command=self.run_analysis).pack()
        
        self.root.mainloop()
    
    def browse_netcdf(self):
        self.netcdf_path.set(filedialog.askopenfilename(filetypes=[("NetCDF", "*.nc")]))
    
    def browse_csv(self):
        self.csv_path.set(filedialog.askopenfilename(filetypes=[("CSV", "*.csv")]))
    
    def run_analysis(self):
        try:
            # Carrega dados e calcula impacto
            waves, winds = load_netcdf_data(self.netcdf_path.get())
            risk_map = calculate_impact(waves, self.wave_threshold.get())
            
            # Gera mapa Folium
            lat_lon = [-23.5, -45.0]  # Coordenadas aproximadas da Bacia de Santos
            create_risk_map(risk_map, lat_lon)
            webbrowser.open("outputs/risk_map.html")
            
            # Calcula custos
            risk_days = np.sum(risk_map)  # Dias de risco estimados
            total_loss, report = calculate_losses(self.csv_path.get(), risk_days)
            report.to_csv("outputs/report.csv", index=False)
            
            messagebox.showinfo(
                "Análise Concluída",
                f"""Custo total estimado: R${total_loss:,.2f}\n
                Relatório salvo em outputs/report.csv"""
            )
        except Exception as e:
            messagebox.showerror("Erro", f"Falha na análise: {str(e)}")

if __name__ == "__main__":
    App()
