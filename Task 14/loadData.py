import pandas as pd
import sqlite3

# To load Data from CSV
df_csv = pd.read_csv("data.csv")

# Loading JSON Data
df_json = pd.read_json("data.json")

# Excel
df_excel = pd.read_excel("data.xlsx")

# SQL:
# First, we need to establish a connection to the SQL database:
conn = sqlite3.connect('data.db')
# Then, load the data into a Pandas dataframe using a SQL query:

query = "SELECT * FROM data_table"
df_sql = pd.read_sql(query, conn)