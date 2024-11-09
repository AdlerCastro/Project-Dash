# Project-Dash

Uma dashboard interativa e intuitiva para análise de um dataset de pessoas diagnosticadas com diabetes. A aplicação permite uma visualização clara e dinâmica dos dados, facilitando a exploração de padrões, tendências e insights relacionados aos diferentes tipos de diabetes e suas variáveis associadas.

## 📊 Descrição do Projeto

O **Project-Dash** foi desenvolvido em Python e utiliza as bibliotecas Pandas, Plotly e Streamlit para criar uma interface interativa com gráficos estáticos e dinâmicos. Essa dashboard permite ao usuário filtrar e visualizar os dados de acordo com diferentes faixas etárias e tipos de diabetes, oferecendo uma análise visual direta e eficiente.

## 🚀 Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para todo o desenvolvimento do projeto.
- **Pandas**: Para manipulação e tratamento de dados.
- **Plotly**: Para criação de gráficos e visualizações interativas.
- **Streamlit**: Para construção da interface web e interatividade da aplicação.

## 📌 Funcionalidades

- **Gráficos Estáticos**: Exibição de gráficos informativos que oferecem uma visão geral dos dados.
- **Gráficos Interativos**: Permite a seleção de faixas etárias e tipos de diabetes, ajustando os gráficos em tempo real para uma análise mais personalizada.
- **Análise Exploratória de Dados (EDA)**: Ferramenta poderosa para explorar padrões, detectar outliers, preencher valores ausentes e gerar hipóteses significativas.

## 📂 Estrutura do Projeto
```bash
Project-Dash/
│
├── data/
│   └── diabetes_dataset00.csv       # Dataset utilizado para a análise
│
└── dashboard.py                # Código principal para rodar a dashboard

````
## ⚙️ Como Executar

1. **Clone o repositório**:
```bash
git clone https://github.com/AdlerCastro/Project-Dash.git
cd Project-Dash
````  
2. **Instale as dependências:**
```bash
pip install pandas plotly streamlit
````

3. **Execute a aplicação**
```bash
streamlit run dashboard.py
````

5. **Acesse a dashboard:**
Após a execução, a dashboard estará disponível em
```bash
http://localhost:8501
````
