import pandas as pd
from sqlalchemy import create_engine
import getpass  # for securely entering your password

# Secure MySQL connection info
user = 'root'
password = 'Vaishu%402003'
host = '127.0.0.1'
port = '3306'
database = 'Flight_schedule'

# Set up SQLAlchemy engine
connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(connection_string)

# List of CSV files and target table names
csv_files = ['table_1.csv', 'table_2.csv', 'table_3.csv']
table_names = ['daily_flying_schedule', 'crew_change_412_145', 'crew_change_aw_139']

# Load each CSV and insert into MySQL
for file, table in zip(csv_files, table_names):
    try:
        df = pd.read_csv(file, sep='|')
        df.to_sql(name=table, con=engine, index=False, if_exists='replace')
        print(f"Inserted '{file}' into MySQL table '{table}'")
    except Exception as e:
        print(f"Failed to insert '{file}' into table '{table}': {e}")
