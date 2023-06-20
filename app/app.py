import pandas as pd
from sqlalchemy import create_engine


# MySQL connection details
host = 'mysql-db'
port = 3306
database = 'db_app'
user = 'db_user'
password = 'password'
table_name = 'sample_data'

# Establish MySQL connection through a SQLAlchemy engine
mysql_connection = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')


#Load data from MySQL to a DataFrame
query = f'SELECT * FROM {table_name}'

df_query_result = pd.read_sql(query, mysql_connection)

print(df_query_result.head())

# Close the MySQL connection
mysql_connection.dispose()