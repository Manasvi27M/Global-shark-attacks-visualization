import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Load data from Excel sheet
df = pd.read_excel('global_shark_attacks.xlsx', header=0)

# Extract country names, total attacks, and fatal attacks
countries = df['Country'].tolist()
total_attacks = df['Total'].tolist()
fatal_deaths = df['Fatal'].tolist()

# Streamlit layout
st.title('Global Shark Attacks Data Visualization')
st.write("This app allows you to explore global shark attacks and fatality rates.")

# Create a slider for selecting the country
country_index = st.slider('Select a country:', 0, len(countries)-1, 0, step=1, format="Country: %s")

# Define function to plot pie chart
def update_pie_chart(country_index):
    plt.figure(figsize=(10, 8))
    labels = ['Total', 'Fatal']
    sizes = [total_attacks[country_index], fatal_deaths[country_index]]
    plt.pie(sizes, labels=labels, explode=(0.1, 0), autopct='%1.1f%%', startangle=90, colors=['pink', 'crimson'], shadow=True)
    plt.title('Total attacks vs. Fatal attacks in {}'.format(countries[country_index]))
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    st.pyplot(plt)

# Call function to update pie chart based on selected country
update_pie_chart(country_index)
