import numpy as np
import netCDF4 as nc
from climada.engine import Impact

def load_netcdf_data(netcdf_path):
    """Carrega dados meteorológicos/oceanográficos."""
    data = nc.Dataset(netcdf_path)
    waves = data.variables['wave_height'][:]  # Exemplo: altura das ondas
    winds = data.variables['wind_speed'][:]   # Exemplo: velocidade do vento
    return waves, winds

def calculate_impact(waves, threshold=2.0):
    """Retorna um mapa de risco binário (1 = perigo, 0 = seguro)."""
    return np.where(waves > threshold, 1, 0)

