📊 Dashboard de Análise Estatística
Este projeto é um dashboard interativo de análise de dados, desenvolvido com um backend em Python (Flask) e um frontend em React.
A aplicação lê um conjunto de dados meteorológicos de um arquivo .csv, realiza uma série de análises estatísticas descritivas e de regressão, e exibe os resultados em gráficos e tabelas interativas.
✨ Funcionalidades
1. Análise Estatística Descritiva
O dashboard calcula e exibe as principais métricas estatísticas para todas as colunas numéricas dos dados:
 * Média
 * Mediana
 * Moda
 * Variância
 * Desvio Padrão
 * Matriz de Covariância
2. Visualização Interativa
Os dados descritivos podem ser visualizados de forma dinâmica através de um seletor de gráficos:
 * Gráfico de Barras
 * Gráfico de Linhas
 * Gráfico de Áreas
 * Gráfico de Setores (Pizza)
 * Gráfico de Radar
3. Análise de Regressão
A aplicação realiza uma análise de regressão profunda, comparando múltiplos modelos para prever a relação entre duas variáveis (ex: Radiação Solar vs. Temperatura).
 * Modelos Implementados:
   * Regressão Linear
   * Regressão Polinomial (Parábola)
   * Regressão Exponencial
   * Regressão Potência
   * Regressão Logística
 * Comparação de Otimização: Compara os resultados do método de Mínimos Quadrados (via Levenberg-Marquardt) com a otimização por Máxima Verossimilhança (MLE).
 * Métricas de Avaliação: Todos os modelos são avaliados e comparados usando R² (Coeficiente de Determinação) e RMSE (Raiz do Erro Quadrático Médio).
4. Conteúdo Teórico
O projeto também serve como um repositório de conhecimento, incluindo o conteúdo textual para apresentação dos seguintes tópicos estatísticos:
 * Teorema Central do Limite
 * Correlação
 * Amostragem e Distribuição Normal (Curva de Gauss)
 * Teste t-Student
 * Teste Qui-Quadrado
💻 Tecnologias Utilizadas
 * Backend:
   * Python 3.11+
   * Flask (para a API REST)
   * Pandas (para manipulação de dados)
   * Scikit-learn (para modelos lineares e métricas)
   * Scipy (para otimização e modelos não lineares)
   * Waitress (servidor de produção WSGI)
 * Frontend:
   * React
   * JavaScript (ES6+)
   * Axios (para requisições à API)
   * Recharts (para os gráficos)
   * CSS (para estilização)
🚀 Como Executar o Projeto
Siga os passos abaixo para rodar o projeto em sua máquina local.
Pré-requisitos
 * Python 3.10+
 * Node.js (LTS)
 * Git
1. Clone o Repositório
git clone (https://github.com/Wors95/PyDashDc)
cd PyDashDc

(https://github.com/Wors95/PyDashDc)
2. Configure e Inicie o Backend (Terminal 1)
O backend é responsável por toda a análise de dados e pela API.
# Navegue até a pasta do backend
cd backend

# Crie um ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # No macOS/Linux
.\venv\Scripts\activate   # No Windows

# Instale as dependências do Python
pip install flask flask-cors pandas numpy scikit-learn scipy waitress

# Inicie o servidor
python api.py

O servidor estará rodando em http://127.0.0.1:5000.
Mantenha este terminal aberto.
3. Configure e Inicie o Frontend (Terminal 2)
O frontend é a interface visual que você vê no navegador.
# Abra um NOVO terminal
# Navegue até a pasta do frontend
cd frontend

# Instale as dependências do Node.js
npm install

# Inicie o servidor de desenvolvimento do React
npm start

O seu navegador abrirá automaticamente no endereço http://localhost:3000.
🔧 Configuração
Para usar seus próprios dados, você precisa:
 * Colocar seu arquivo .csv dentro da pasta backend/.
 * Abrir o arquivo backend/api.py.
 * Atualizar as seguintes variáveis no topo do arquivo com os nomes do seu arquivo e das colunas que deseja analisar:
   ARQUIVO_CSV = 'backend/seu_arquivo.csv'
COLUNA_X_REGRESSAO = 'Nome_da_sua_coluna_X'
COLUNA_Y_REGRESSAO = 'Nome_da_sua_coluna_Y'

 * Lembre-se de que o script está configurado para ler arquivos .csv que usam:
   * Ponto e vírgula (sep=';') como separador.
   * Vírgula (decimal=',') como separador decimal.
   Se seu arquivo for diferente, ajuste a linha pd.read_csv(...) no arquivo backend/analise_regressao.py.
