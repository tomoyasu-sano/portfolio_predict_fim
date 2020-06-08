import settings_path as s
import os
import pandas as pd


def load_df(path_to_df_file):
    if os.path.exists(path_to_df_file):
        ext = os.path.splitext(os.path.basename(path_to_df_file))[1]
        if ext ==".pickle":
            df = pd.read_pickle(path_to_df_file)
    
    #print("ok. df_shape：", df.shape)
    #print(df.columns)
    return df