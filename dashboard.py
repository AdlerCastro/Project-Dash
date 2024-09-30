import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------- VISUALILATION CONFIGS -------------------------------
st.set_page_config(layout='wide')
st.title('Análise de Diabetes')

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

# -------------------- FILTERING -------------------------------

df = pd.read_csv('./data/diabetes_dataset00.csv')
targets = ['Type 1 Diabetes', 'Type 2 Diabetes', 'Prediabetic', 'MODY', 'Wolfram Syndrome']
selected_columns = ['Target', 'Family History', 'Smoking Status', 'Dietary Habits',
                    'Alcohol Consumption', 'Physical Activity', 'Age', 'Birth Weight']

df_filtered = df[df['Target'].isin(targets)]
df_filtered = df_filtered[selected_columns]

#Young ]24], Adult [25,59], Elderly [60[
age_ranges = [0, 24, 59, float('inf')] 
categories_age = ['Young', 'Adult', 'Elderly'] 

df_filtered['Age Range'] = pd.cut(df_filtered['Age'], bins=age_ranges, labels=categories_age, right=True)

age_selection = st.sidebar.selectbox('Select the age range:', ['Young', 'Adult', 'Elderly'])
target_selection = st.sidebar.selectbox('Select the diabetes type:', targets)

filtered_by_age_target = df_filtered[
    (df_filtered['Age Range'] == age_selection) &
    (df_filtered['Target'] == target_selection)
]

# -------------------- TARGETS COUNT -------------------------------

target_counts = df_filtered['Target'].value_counts().reset_index()
target_counts.columns = ['Diabete', 'Quantity']

fig_pie_target_counts = px.pie(target_counts, 
    names="Diabete", 
    values='Quantity', 
    title='Distribution by type'
)

# -------------------- AGE RANGE COUNT -------------------------------
age_range_counts = df_filtered['Age Range'].value_counts().reset_index()
age_range_counts.columns = ['Age Range','Quantity']

fig_pie_ar_counts = px.pie(age_range_counts,
    names='Age Range',
    values='Quantity',
    title='Distribution by Age Range'
)

# -------------------- HEALTHY X NO HEALTHY PREDIABETICS ADULTS (NO FAM. HIST) -------------------------------

healthy = filtered_by_age_target[
    (filtered_by_age_target['Family History']  == 'No') & 
    (filtered_by_age_target['Smoking Status']  == 'Non-Smoker') &
    (filtered_by_age_target['Dietary Habits']  == 'Healthy') &
    (filtered_by_age_target['Alcohol Consumption']  == 'Low') &
    (filtered_by_age_target['Physical Activity'] == 'High')
    ].shape[0]

unhealthy = filtered_by_age_target[
    (filtered_by_age_target['Family History']  == 'No') & 
    (filtered_by_age_target['Smoking Status']  == 'Smoker') &
    (filtered_by_age_target['Dietary Habits']  == 'Unhealthy') &
    (filtered_by_age_target['Alcohol Consumption'].isin(['High', 'Moderate'])) &
    (filtered_by_age_target['Physical Activity'] == 'Low')
    ].shape[0]

healthy_unhealthy = pd.DataFrame({
    'Status': ['Saudáveis','Não Saudáveis'],
    'Quantity': [healthy, unhealthy]
})

fig_bar_healthy_unhealthy = px.bar(healthy_unhealthy, 
x='Status', 
y='Quantity', 
title='Healthy x Non-Healthy'
)

# -------------------- WITH X WITHOUT FAM HIST YOUNGS -------------------------------

histfam = filtered_by_age_target[
    (filtered_by_age_target['Family History']  == 'Yes') & 
    (filtered_by_age_target['Smoking Status']  == 'Non-Smoker') &
    (filtered_by_age_target['Dietary Habits']  == 'Healthy') &
    (filtered_by_age_target['Alcohol Consumption']  == 'Low') &
    (filtered_by_age_target['Physical Activity'] == 'High')   
    ].shape[0]

no_histfam = filtered_by_age_target[
    (filtered_by_age_target['Family History']  == 'No') & 
    (filtered_by_age_target['Smoking Status']  == 'Non-Smoker') &
    (filtered_by_age_target['Dietary Habits']  == 'Healthy') &
    (filtered_by_age_target['Alcohol Consumption']  == 'Low') &
    (filtered_by_age_target['Physical Activity'] == 'High')   
    ].shape[0]

histfam_nohistfam = pd.DataFrame({
    'Status': ['With','Without'],
    'Quantity': [histfam, no_histfam]
})

fig_bar_histfam_nohistfam = px.bar(histfam_nohistfam, 
x='Status', 
y='Quantity', 
title='Healthy With X Without Family History'
)

# -------------------- FRONTEND -------------------------------

with col1:
    st.subheader('Count by type of diabetes')
    st.plotly_chart(fig_pie_target_counts, use_container_width=True)
    
with col2:
    st.subheader('Count by age range') 
    st.plotly_chart(fig_pie_ar_counts, use_container_width=True)

with col3:
    st.subheader("Table with the selected columns:")
    st.dataframe(df_filtered.head())

with col4:
    st.plotly_chart(fig_bar_healthy_unhealthy, use_container_width=True)

with col5:
    st.plotly_chart(fig_bar_histfam_nohistfam, use_container_width=True)
