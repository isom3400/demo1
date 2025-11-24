
Practice Title: Displaying Real-World Data in Streamlit
Project Objective
In this practice, you’ll use a real-world dataset to build a Streamlit app that reads a CSV file, loads it into a DataFrame, and displays it in an interactive table. We’ll work with a sample dataset, winequality-red.csv, but you can replace it with any other dataset in CSV format if you prefer.

Instructions
Download the winequality-red.csv file:
You can download it from the UCI Machine Learning Repository here.

Save the file in your current working directory:
This will allow the code to locate and load it easily.

Use the Code Template Below:
The code provided reads the CSV file winequality-red.csv and displays it in an interactive table using Streamlit.

Code Template
import streamlit as st
import pandas as pd
import os

# Get the current working directory
current_directory = os.getcwd()
# Define the file path
file_path = os.path.join(current_directory, 'winequality-red.csv')

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path, delimiter=';')

# Display the DataFrame in an interactive table
st.write("Wine Quality Data")
st.dataframe(df)
