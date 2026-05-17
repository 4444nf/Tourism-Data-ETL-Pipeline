from sqlalchemy import create_engine
import configparser
import pandas as pd


data = pd.read_excel("test.xlsx", sheet_name="T2.2.6",skiprows=1)
data_cleaned = data.dropna()

config = configparser.ConfigParser()
config.read('database.ini')

db = config["database"]

connection_string = (
    f"postgresql+psycopg2://{db['user']}:{db['password']}"
    f"@{db['host']}:{db['port']}/{db['name']}"
)

engine = create_engine(connection_string)
data_cleaned.to_sql("turizmus", engine, if_exists="replace", index=False)

df_long = data_cleaned.melt(
    id_vars=["Tourist region"],
    value_vars=["Overnight stays 2019", "Overnight stays 2020", "Overnight stays 2021", "Overnight stays 2022", "Overnight stays 2023"],
    var_name= "Year",
    value_name="Overnight stays"
)
df_long["Year"] = df_long["Year"].str.extract(r'(\d{4})')