import numpy as np
import netCDF4 as nc

def load_meteorological_data(netcdf_path):
    """Carrega dados meteorológicos do arquivo NetCDF."""
    dataset = nc.Dataset(netcdf_path)
    
    # Carregar variáveis relevantes
    precipitation = dataset.variables['apcpsfc'][:]  # Total precipitation [kg/m^2]
    wind_gusts = dataset.variables['gustsfc'][:]      # Surface wind gust [m/s]
    temperature = dataset.variables['tmp2m'][:]        # 2 m above ground Temp. [K]
    
    return precipitation, wind_gusts, temperature

def load_oceanographic_data(netcdf_path):
    """Carrega dados oceanográficos do arquivo NetCDF."""
    dataset = nc.Dataset(netcdf_path)
    
    # Carregar variáveis relevantes
    wave_height = dataset.variables['hs'][:]           # Sea surface wave significant height
    peak_period = dataset.variables['tp'][:]            # Sea surface wave peak period
    
    return wave_height, peak_period

def calculate_hazard(precipitation, wind_gusts, wave_height, threshold_wave=2.0):
    """Calcula o risco baseado nas variáveis meteorológicas e oceanográficas."""
    # Exemplo de lógica para determinar risco
    risk_map = np.zeros_like(wave_height)  # Inicializa o mapa de risco
    
    # Condições de risco
    risk_map[(wave_height > threshold_wave) | (wind_gusts > 15)] = 1  # Exemplo: ondas > 2m ou vento > 15 m/s
    
    return risk_map

