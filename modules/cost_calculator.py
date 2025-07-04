import pandas as pd

def calculate_losses(vessels_csv, risk_days):
    """
    vessels_csv: caminho para o CSV das embarcações  
    risk_days: dias em que região está em risco  
    Retorna: custo total e relatório por embarcação.
    """
    df = pd.read_csv(vessels_csv)
    df['daily_loss'] = df['day_rate'] * risk_days
    total_loss = df['daily_loss'].sum()
    return total_loss, df

