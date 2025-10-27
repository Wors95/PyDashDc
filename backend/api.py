# backend/api.py

from flask import Flask, jsonify, Response
from flask_cors import CORS
# Adicionamos a nova função aqui
from analise_regressao import executar_analise_com_arquivo, calcular_estatisticas_descritivas
import numpy as np
import pandas as pd

app = Flask(__name__)
CORS(app)

# --- CONFIGURAÇÃO ---
ARQUIVO_CSV = 'backend/meus_dados.csv'
COLUNA_X_REGRESSAO = 'RADIACAO GLOBAL (Kj/m²)'
COLUNA_Y_REGRESSAO = 'TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)'
# ------------------------------------

print("Iniciando análise do arquivo...")
df_dados, resultados_analise = executar_analise_com_arquivo(ARQUIVO_CSV, COLUNA_X_REGRESSAO, COLUNA_Y_REGRESSAO)

if df_dados is None:
    raise RuntimeError("Falha ao carregar e analisar os dados para regressão.")
else:
    print("Análise de regressão concluída. Servidor pronto.")

# --- ROTAS DA API ---

@app.route('/api/data', methods=['GET'])
def get_data():
    if not isinstance(df_dados, pd.DataFrame):
        return jsonify({"error": "Formato de dados interno inválido"}), 500
    df_renomeado = df_dados.rename(columns={COLUNA_X_REGRESSAO: 'X', COLUNA_Y_REGRESSAO: 'y'})
    json_string = df_renomeado.to_json(orient='records')
    return Response(json_string, mimetype='application/json')

@app.route('/api/results', methods=['GET'])
def get_results():
    json_ready_results = {}
    for metodo, res in resultados_analise.items():
        json_ready_results[metodo] = {'R2': None if np.isnan(res['R2']) else res['R2'], 'RMSE': None if np.isnan(res['RMSE']) else res['RMSE'], 'predicoes': res['predicoes'].tolist(), 'params': res.get('params', {})}
    return jsonify(json_ready_results)

# --- NOVA ROTA PARA ESTATÍSTICAS ---
@app.route('/api/statistics', methods=['GET'])
def get_statistics():
    # Carrega o dataframe original novamente para ter todas as colunas
    df_original = pd.read_csv(ARQUIVO_CSV, encoding='latin-1', sep=';', decimal=',')
    
    # Seleciona apenas as colunas que são numéricas para as estatísticas
    colunas_numericas = df_original.select_dtypes(include=np.number).columns.tolist()

    # Calcula as estatísticas
    estatisticas = calcular_estatisticas_descritivas(df_original, colunas_numericas)
    
    return jsonify(estatisticas)


if __name__ == '__main__':
    print("Iniciando a API Flask na porta 5000...")
    app.run(debug=True)