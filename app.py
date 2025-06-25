# Full Streamlit App for Advanced iFood Campaign Analytics
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import plotly.express as px

# Load Data
data = pd.read_csv('ifood_df.csv')

# Preprocessing
def preprocess_data(data):
    data.fillna(data.median(numeric_only=True), inplace=True)
    data.drop_duplicates(inplace=True)
    return data

data = preprocess_data(data)

# Streamlit Setup
st.set_page_config(page_title='iFood Campaign Analytics', layout='wide', page_icon='📊')
st.title('📊 iFood Campaign Marketing Analytics Dashboard')

# Sidebar Filters
st.sidebar.header("Filter Options")
min_income, max_income = st.sidebar.slider("Select Income Range", int(data['Income'].min()), int(data['Income'].max()), (10000, 80000))
filtered_data = data[(data['Income'] >= min_income) & (data['Income'] <= max_income)]

# EDA Section
st.subheader("🔍 Exploratory Data Analysis")
st.write("**Summary Statistics**")
st.dataframe(filtered_data.describe())

col1, col2 = st.columns(2)
with col1:
    fig = px.histogram(filtered_data, x='Response', color='Kidhome', barmode='group', title='Response Distribution by Kidhome')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    corr = filtered_data.corr(numeric_only=True)
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, cmap='coolwarm', annot=False, ax=ax)
    st.pyplot(fig)

# A/B Test Results
st.subheader("📊 A/B Testing on Campaigns")
def perform_ab_testing(data):
    campaigns = [f'AcceptedCmp{i}' for i in range(1, 6)]
    results = {}
    for campaign in campaigns:
        response = data[data[campaign] == 1]['Response']
        no_response = data[data[campaign] == 0]['Response']
        stat, pval = ttest_ind(response, no_response, equal_var=False, nan_policy='omit')
        results[campaign] = {'t-statistic': stat, 'p-value': pval}
    return results

ab_results = perform_ab_testing(filtered_data)
ab_df = pd.DataFrame(ab_results).T
st.dataframe(ab_df.style.format({"t-statistic": "{:.2f}", "p-value": "{:.4f}"}))

# PCA Section
st.subheader("📉 Dimensionality Reduction (PCA)")
def perform_pca(data):
    numeric_features = data.select_dtypes(include=['float64', 'int64'])
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(numeric_features)
    pca = PCA(n_components=5)
    pca_data = pca.fit_transform(scaled_data)
    explained_variance = pca.explained_variance_ratio_
    return explained_variance

explained_variance = perform_pca(filtered_data)
st.bar_chart(pd.Series(explained_variance, index=[f'PC{i+1}' for i in range(len(explained_variance))]))

# Insights
st.subheader("💡 Insights")
col1, col2 = st.columns(2)
with col1:
    overall_response = filtered_data['Response'].mean()
    st.metric("Overall Response Rate", f"{overall_response:.2%}")
    complaints = filtered_data['Complain'].mean()
    st.metric("Customer Complaint Rate", f"{complaints:.2%}")

with col2:
    best_campaign = max([f'AcceptedCmp{i}' for i in range(1, 6)], key=lambda x: filtered_data[x].mean())
    rate = filtered_data[best_campaign].mean()
    st.metric("Best Performing Campaign", f"{best_campaign} ({rate:.2%})")

# Spending
spending = filtered_data[['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']].mean()
st.bar_chart(spending)

st.success("Dashboard Loaded Successfully! Explore insights and optimize your marketing campaigns.")
