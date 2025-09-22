import openpyxl
import pandas
import xlrd
from sqlalchemy import create_engine
import psycopg2
import openpyxl

import pandas as pd

# Load the dataset
data = pd.read_excel("test.xlsx", sheet_name="T2.2.6",skiprows=1)
print(data.head())
data_cleaned = data.dropna()
print(data_cleaned.head())

engine = create_engine("postgresql://postgres:postgres@localhost:5432/postgres")
data.to_sql("turizmus", engine, if_exists="replace", index=False)

df_long = data.melt(
    id_vars=["Tourist region"],
    value_vars=["Overnight stays 2019", "Overnight stays 2020", "Overnight stays 2021", "Overnight stays 2022", "Overnight stays 2023"],
    var_name= "Year",
    value_name="Overnight stays"
)
df_long["Year"] = df_long["Year"].str.extract(r'(\d{4})')

