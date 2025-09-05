import pandas as pd
from sqlalchemy import create_engine


user = 'root'
password = 'venkat'
host = 'localhost'
database = 'cdta_db'

mysql_conn_str = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"

df = pd.read_csv('C:/Users/venka/Downloads/agg_data.csv')

engine = create_engine(mysql_conn_str)
table_name = 'agri_data'
    
df.to_sql(table_name, con=engine, if_exists='replace', index=False)
print("Database setup complete. Data loaded into agri_data table.")




