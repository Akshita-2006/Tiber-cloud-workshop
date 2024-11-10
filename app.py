import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('loan_approval_dataset.csv')  #reading data from csv wali file

# Streamlit code to create the user interface
st.title('Loan prediction model')

# Display DataFrame
st.write(data)

# Visualization (Example)
st.write("Data Visualization")
sns.heatmap(data.corr())
st.pyplot()