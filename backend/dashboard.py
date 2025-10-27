# backend/dashboard.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from analise_regressao import executar_analise # Importa nossa função principal

st.set_page_config(layout="wide")

# --- Título e Cabeçalho ---
st.title("📊 Dashboard de Análise de Regressão")
st.markdown("""
Este dashboard apresenta os resultados da aplicação de diferentes modelos de regressão 
em um conjunto de dados sintético com padrão exponencial.
""")

# --- Executa a análise (os resultados ficam em cache para performance) ---
@st.cache_data
def carregar_dados_e_analise():
    df, resultados = executar_analise()
    return df, resultados

df, resultados = carregar_dados_e_analise()

# --- Layout do Dashboard em Colunas ---
col1, col2 = st.columns((1, 1.5)) # Coluna 1 menor que a 2

with col1:
    st.header("Dados Originais")
    st.write(df)

    st.header("Comparativo de Métodos")
    st.markdown("Avaliação dos modelos com base no R² (quanto mais perto de 1, melhor) e RMSE (quanto menor, melhor).")
    
    tabela_resultados = pd.DataFrame({
        metodo: {'R2': v['R2'], 'RMSE': round(v['RMSE'], 2)}
        for metodo, v in resultados.items()
    }).T
    
    st.table(tabela_resultados)

    st.markdown("""
    **Conclusão:** Os modelos não-lineares (LM e MLE) se ajustaram muito melhor aos dados do que o modelo linear, como indicado pelos valores de R² e RMSE.
    """)

with col2:
    st.header("Visualização Gráfica das Regressões")

    fig, ax = plt.subplots(figsize=(12, 7))

    # Plot dos dados originais
    sns.scatterplot(x='X', y='y', data=df, ax=ax, label='Dados Originais', color='blue', s=50)

    # Plot das linhas de regressão
    for metodo, result in resultados.items():
        ax.plot(df['X'], result['predicoes'], label=f"{metodo} (R²={result['R2']:.2f})")

    ax.set_title("Comparação dos Modelos de Regressão", fontsize=16)
    ax.set_xlabel("Variável Independente (X)", fontsize=12)
    ax.set_ylabel("Variável Dependente (y)", fontsize=12)
    ax.legend()
    ax.grid(True)
    
    st.pyplot(fig)