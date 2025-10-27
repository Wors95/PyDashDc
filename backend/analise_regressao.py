# backend/analise_regressao.py

import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score, mean_squared_error

# --- FUNÇÕES DE MODELO (sem alteração) ---
def modelo_exponencial(x, a, b):
    return a * np.exp(b * x)
def modelo_potencia(x, a, b):
    return a * np.power(x + 1e-6, b)
def modelo_logistico(x, L, k, x0):
    return L / (1 + np.exp(-k * (x - x0)))

# --- FUNÇÃO DE ANÁLISE DE REGRESSÃO (sem alteração) ---
def executar_analise_com_arquivo(filepath, coluna_x, coluna_y):
    # (Todo o código desta função que já fizemos continua aqui, sem alterações)
    # ...
    try:
        df = pd.read_csv(filepath, encoding='latin-1', sep=';', decimal=',')
    except FileNotFoundError:
        return None, None
    if coluna_x not in df.columns or coluna_y not in df.columns:
        return None, None
    df[coluna_x] = pd.to_numeric(df[coluna_x], errors='coerce')
    df[coluna_y] = pd.to_numeric(df[coluna_y], errors='coerce')
    df.dropna(subset=[coluna_x, coluna_y], inplace=True)
    if 'RADIACAO' in coluna_x.upper():
        df = df[df[coluna_x] > 50]
    if df.empty:
        return None, None
    df = df.sort_values(by=coluna_x).reset_index(drop=True)
    X = df[coluna_x].values
    y = df[coluna_y].values
    X_reshaped = X.reshape(-1, 1)
    resultados = {}
    model_linear = LinearRegression()
    model_linear.fit(X_reshaped, y)
    y_pred_linear = model_linear.predict(X_reshaped)
    resultados['Regressao Linear'] = {'R2': r2_score(y, y_pred_linear), 'RMSE': np.sqrt(mean_squared_error(y, y_pred_linear)), 'predicoes': y_pred_linear, 'params': {}}
    model_poly = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
    model_poly.fit(X_reshaped, y)
    y_pred_poly = model_poly.predict(X_reshaped)
    resultados['Regressao Polinomial'] = {'R2': r2_score(y, y_pred_poly), 'RMSE': np.sqrt(mean_squared_error(y, y_pred_poly)), 'predicoes': y_pred_poly, 'params': {}}
    try:
        params_exp, _ = curve_fit(modelo_exponencial, X, y, p0=[1, 0.0001], maxfev=10000)
        y_pred_exp = modelo_exponencial(X, *params_exp)
        resultados['Regressao Exponencial'] = {'R2': r2_score(y, y_pred_exp), 'RMSE': np.sqrt(mean_squared_error(y, y_pred_exp)), 'predicoes': y_pred_exp, 'params': {}}
    except (RuntimeError, ValueError):
        resultados['Regressao Exponencial'] = {'R2': np.nan, 'RMSE': np.nan, 'predicoes': np.zeros_like(y), 'params': {}}
    
    return df, resultados

# --- NOVA FUNÇÃO PARA ESTATÍSTICAS DESCRITIVAS ---
def calcular_estatisticas_descritivas(df, colunas_interesse):
    """Calcula as principais estatísticas descritivas para as colunas numéricas de interesse."""
    
    # Seleciona apenas as colunas de interesse e garante que são numéricas
    df_stats = df[colunas_interesse].apply(pd.to_numeric, errors='coerce').dropna()
    
    stats = {
        'media': df_stats.mean().to_dict(),
        'mediana': df_stats.median().to_dict(),
        'moda': df_stats.mode().iloc[0].to_dict(), # Pega a primeira moda se houver mais de uma
        'variancia': df_stats.var().to_dict(),
        'desvio_padrao': df_stats.std().to_dict(),
        'covariancia': df_stats.cov().to_dict('index') # Matriz de covariância
    }
    return stats