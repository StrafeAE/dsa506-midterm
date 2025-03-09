import streamlit as st
import plotly.express as px
import pandas as pd


st.title("University Admissions Dashboard")
df = pd.read_csv('university_student_dashboard_data.csv')

col1, col2, col3 = st.columns((3))

st.sidebar.header("Choose your filter: ")
# Create for Year
year = st.sidebar.multiselect("Pick your Year", df["Year"].unique())
term = st.sidebar.multiselect("Pick the Term", df["Term"].unique())

filtered = df.copy()
if year:
    filtered = filtered[filtered['Year'].isin(year)]
if term:
    filtered = filtered[filtered['Term'].isin(term)]

with col1:
    st.metric('Applications', filtered['Applications'].sum())
with col2:
    st.metric('Admitted', filtered['Admitted'].sum())
with col3:
    st.metric('Enrolled', filtered['Enrolled'].sum())

major_breakdown = px.bar(filtered, x=px.Constant('Major'), y=['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled'])
major_breakdown.update_layout(barmode='group')
st.plotly_chart(major_breakdown)

col_a, col_b = st.columns((2))

with col_a:
    retention_graph = px.line(df, x='Year', y='Retention Rate (%)', title='Student Retention Rate')
    st.plotly_chart(retention_graph, use_container_width=True)
with col_b:
    satisfaction_graph = px.line(df, x='Year', y='Student Satisfaction (%)', title='Student Satisfaction Score')
    st.plotly_chart(satisfaction_graph)
