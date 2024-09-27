import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('./data/diabetes_dataset00.csv')

# -------------------- FILTRANDO OS TARGETS -------------------------------
# Filtrar os três tipos de diabetes 
df_filtered = df[df['Target'].isin(['Type 1 Diabetes', 'MODY', 'Wolfram Syndrome'])]

# -------------------- VISUALIZAÇÃO -------------------------------
st.set_page_config(layout="wide")
st.title('Análise de Diabetes')

# Divisão de colunas para os gráficos
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# -------------------- GRÁFICO PIZZA CONTAGEM -------------------------------

# Agrupando dados de 'Target' e contando quantos de cada tipo existem
target_counts = df_filtered['Target'].value_counts().reset_index()
target_counts.columns = ['Tipo', 'Quantidade']

# Gráfico de pizza (coluna 'Tipo' são as fatias e 'Quantidade' o tamanho de cada fatia)
fig_pie_target_counts = px.pie(target_counts, names='Tipo', values='Quantidade', 
                               title='Distribuição de Tipos de Diabetes')

# Exibir os gráficos nas colunas
with col1:
    st.subheader('Contagem por Tipo de Diabetes')
    st.write("Tabela de Quantidade por Tipo de Diabetes")
    st.write(target_counts)  # Exibindo a tabela com os dados

with col2:
    st.plotly_chart(fig_pie_target_counts, use_container_width=True)  # Gráfico de pizza

# -------------------- GRÁFICO BARRA FAM HIST -------------------------------
fig_hf_target = px.bar(df_filtered, x='Target', color='Family History', 
                       title='Distribuição de Histórico Familiar por Tipo de Diabetes')

with col3:
    st.subheader('Distribuição de Histórico Familiar por Tipo de Diabetes')
    st.plotly_chart(fig_hf_target, use_container_width=True)

# -------------------- GRÁFICO BOXPLOT BIRTH WEIGHT -------------------------------
fig_bw_target = px.box(df_filtered, x='Target', y='Birth Weight', 
                       title='Distribuição do Peso ao Nascer por Tipo de Diabetes')
with col4:
    st.subheader('Distribuição do Peso ao Nascer por Tipo de Diabetes')
    st.plotly_chart(fig_bw_target, use_container_width=True)

# -------------------- GRÁFICO BARRA SOC FACTORS -------------------------------
st.subheader('Distribuição de Fatores Socioeconômicos por Tipo de Diabetes')
fig_fse_target = px.bar(df_filtered, x='Target', color='Socioeconomic Factors', 
                        title='Distribuição de Fatores Socioeconômicos por Tipo de Diabetes')
                        
st.plotly_chart(fig_fse_target, use_container_width=True)
