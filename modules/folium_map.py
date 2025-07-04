import folium
import numpy as np

def create_risk_map(risk_data, lat_lon_bounds):
    """Gera HTML com mapa de calor Folium."""
    m = folium.Map(location=[lat_lon_bounds[0], lat_lon_bounds[1]], zoom_start=8)
    
    # Adiciona heatmap (exemplo simplificado)
    for y in range(risk_data.shape[0]):
        for x in range(risk_data.shape[1]):
            if risk_data[y, x] == 1:  # Risco detectado
                folium.CircleMarker(
                    location=[lat_lon_bounds[0] + y*0.01, lat_lon_bounds[1] + x*0.01],
                    radius=5,
                    color='red',
                    fill=True
                ).add_to(m)
    
    m.save("outputs/risk_map.html")
    return m

