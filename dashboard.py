import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------- FILTERING TARGETS-------------------------------
df = pd.read_csv('./data/diabetes_dataset00.csv')
targets = ['Type 1 Diabetes', 'Type 2 Diabetes', 'Prediabetic', 'MODY', 'Wolfram Syndrome']
selected_columns = ['Target', 'Family History', 'Smoking Status', 'Dietary Habits',
                    'Alcohol Consumption', 'Physical Activity', 'Age', 'Birth Weight']

df_filtered = df[df['Target'].isin(targets)]
df_filtered = df_filtered[selected_columns]

# -------------------- AGE RANGES -------------------------------
age_ranges = [0, 24, 59, float('inf')] 
categories_age = ['Young', 'Adult', 'Elderly'] 
df_filtered['Age Range'] = pd.cut(df_filtered['Age'], bins=age_ranges, labels=categories_age, right=True)

# -------------------- VISUALIZATION CONFIGS -------------------------------
st.set_page_config(layout='wide')
st.title('Análise de Diabetes')

age_selection = st.sidebar.selectbox('Select the age range:', ['Young', 'Adult', 'Elderly'])
target_selection = st.sidebar.selectbox('Select the diabetes type:', targets)

filtered_by_target = df_filtered[df_filtered['Target'] == target_selection]

filtered_by_age = df_filtered[df_filtered['Age Range'] == age_selection]

filtered_by_age_target = df_filtered[
    (df_filtered['Age Range'] == age_selection) &
    (df_filtered['Target'] == target_selection)
]

col1, col2, col3 = st.columns(3)
col4, col5, col6, col7,  = st.columns(4)

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
age_range_counts.columns = ['Age Range', 'Quantity']

fig_bar_ar_counts = px.bar(age_range_counts,
    x='Quantity', 
    y='Age Range', 
    orientation='h',
    title='Distribution by Age Range'
)

# -------------------- AGE RANGE COUNT -------------------------------
age_target_trend = df_filtered.groupby(['Age', 'Target']).size().reset_index(name='Count')

fig_age_target_trend = px.scatter(age_target_trend, 
    x='Age', 
    y='Count', 
    color='Target',  
    title='Diabetes Types Distribution by Age',
    labels={'Count': 'Number of Cases'},  
    trendline='lowess'  
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

# -------------------- PROBABILITY OF AGE RANGE -------------------------------

ar_prob = filtered_by_target['Age Range'].value_counts().reset_index()
ar_prob.columns = ['Age Range', 'Total']

fig_ar_prob = px.pie(ar_prob,
    names='Age Range',
    values='Total',
    title=f'Possible Age Range for {target_selection}'
)

# -------------------- Total OF DIABETES -------------------------------
target_prob = filtered_by_age['Target'].value_counts().reset_index()
target_prob.columns = ['Target', 'Total']

fig_target_prob = px.pie(target_prob,
    names='Target',
    values='Total',
    title=f'Possible Diabetes tye for {age_selection}'
)
# -------------------- FRONTEND -------------------------------

with col1:
    st.subheader('Age ranges') 
    st.plotly_chart(fig_bar_ar_counts, use_container_width=True)

with col2:
    st.subheader('Types of diabetes')
    st.plotly_chart(fig_pie_target_counts, use_container_width=True) 

with col3:
    st.subheader('Age Trend by Type of Diabetes')
    st.plotly_chart(fig_age_target_trend, use_container_width=True)

with col4:
    st.plotly_chart(fig_bar_healthy_unhealthy, use_container_width=True)

with col5:
    st.plotly_chart(fig_bar_histfam_nohistfam, use_container_width=True)

with col6:
    st.plotly_chart(fig_ar_prob, use_container_width=True)

with col7:
    st.plotly_chart(fig_target_prob, use_container_width=True)