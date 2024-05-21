import pandas as pd
import os
import glob

directory = "D:/join csv/csv_training_data"
csv_files = glob.glob(f'{directory}/*.csv')
dfs = []
for i, file in enumerate(csv_files):
    df = pd.read_csv(file,header=0,usecols=["path","Xmin","Ymin","Xmax","Ymax","classLabel"])
    dfs.append(df)
concatenated_df = pd.concat(dfs)
concatenated_df.to_csv('D:/join csv/retinanet_train_data.csv', index=False)
print("CSV files have been successfully concatenated without headers except for the first one.")
