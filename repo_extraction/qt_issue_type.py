import pandas as pd

json_file_path = '0_999.json'
df = pd.read_json(json_file_path)
print(df.head())