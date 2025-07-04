import numpy as np
import pandas as pd
import xarray as xr  # Para ler NetCDF
from climada.hazard import Hazard
from climada.exposure import Exposure
from climada.engine import Impact
import geopandas as gpd
from shapely.geometry import Point

def load_ocean_data(netcdf_path):
    """Carrega dados oceanográficos do NetCDF."""
    ds = xr.open_dataset(netcdf_path)
    return ds

def create_hazard_map(data, threshold=2.0, hazard_type='waves'):
    """Cria um objeto Hazard do CLIMADA baseado em limiares de risco."""
    if hazard_type == 'waves':
        # Exemplo: risco onde ondas > 2m
        intensity = np.where(data['wave_height'] > threshold, 1, 0)
    elif hazard_type == 'wind':
        # Adapte para outras variáveis
        intensity = np.where(data['wind_speed'] > 30, 1, 0)
    
    hazard = Hazard.from_raster(
        intensity=intensity,
        geometry=data['lon'].values,
        geometry=data['lat'].values,
        crs="EPSG:4326"  # Sistema de coordenadas WGS84
    )
    return hazard

def load_vessels(csv_path):
    """Carrega dados das embarcações e converte para Exposure do CLIMADA."""
    df = pd.read_csv(csv_path)
    exposure = Exposure()
    exposure.gdf = gpd.GeoDataFrame(
        df,
        geometry=[Point(xy) for xy in zip(df['longitude'], df['latitude'])]
    )
    exposure.set_geometry_points()  # Configura pontos geográficos
    return exposure

def calculate_impact(hazard, exposure):
    """Calcula impacto financeiro e retorna hotspots."""
    impact = Impact()
    impact.calc(exposure, hazard)
    return impact

def generate_cost_analysis(impact, daily_rate):
    """Calcula custos operacionais baseados no impacto."""
    downtime_days = impact.impact_matrix.sum(axis=1)  # Dias de risco por embarcação
    total_cost = downtime_days * daily_rate
    return pd.DataFrame({
        'vessel_id': exposure.gdf['id'],
        'downtime_days': downtime_days,
        'total_cost': total_cost
    })

