import os
import pandas as pd
from sqlalchemy import create_engine


db_user = 'root'
db_pass = 'password'
db_host = 'localhost'
db_name = 'shop_nest'
csv_folder_path = r'C:\Users\USER\Desktop\skillovilla\shop_nest_csvs'



engine = create_engine(f"mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}")


for file in os.listdir(csv_folder_path):
    if file.endswith('.csv'):
        table_name = os.path.splitext(file)[0].lower()
        file_path = os.path.join(csv_folder_path, file)
        print(f"Uploading {file} as table '{table_name}'")
        try:
            df = pd.read_csv(file_path)
            df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
            print(f"Uploaded '{table_name}' successfully.")
        except Exception as e:
            print(f"Failed to upload '{table_name}': {e}")

print("All CSV files processed.")


