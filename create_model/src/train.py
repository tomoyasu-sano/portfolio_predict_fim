import os
import pickle
import numpy as np
import pandas as pd
import lightgbm as lgb
import sklearn
from sklearn import model_selection

from materials import column_afters
from model_db import load_df
import settings_path as s



def train(path_to_df_file,path_to_models_dir):
    df = load_df(s.path_to_df_file)

    prediction_columns = column_afters   # 4
    discharge = list(prediction_columns[0])
    almost_prediction_columns = list(prediction_columns[1]) + list(prediction_columns[2]) + list(prediction_columns[3])
    all_prediction_columns = discharge + almost_prediction_columns 

    # 多クラス問題の場合[1-7]→[0-6]に変更する必要がある
    df[almost_prediction_columns] = df[almost_prediction_columns] - 1


    results = {}
    results_home = {}

    for length_value in range(len(prediction_columns)):
        #length = int(df.shape[0]*0.2)
        #arr = np.empty([length, ])

        for col in prediction_columns[length_value]:
            df_pre = df.drop(all_prediction_columns,  axis=1)
            df_pre = df_pre.drop("id", axis=1)

            X = df_pre
            y = df[col]

            X_train , X_test , y_train , y_test= model_selection.train_test_split(X,y, train_size=0.50, random_state=1)
            lgb_train = lgb.Dataset(X_train, y_train)
            lgb_eval = lgb.Dataset(X_test, y_test)

            if length_value == 0:
                params = {'objective':'binary',}
        
            else:
                params = {
                    'objective': 'multiclass',
                    'num_class':7,
                        }

            gbm = lgb.train(params,
                    lgb_train,
                    valid_sets=lgb_eval,
                    num_boost_round=100,
                    )
            
            filename = s.path_to_models_dir+ col +  "_LGBM.pkl"
            pickle.dump(gbm, open(filename, 'wb'))
        
            #テストデータの予測
            if length_value == 0:
                predicted_home = gbm.predict(X_test,num_iteration=gbm.best_iteration)
                
                y_pred_home = []
                for x in predicted_home:
                    y_pred_home.append(np.round(x))

                y_pred_home = np.array(y_pred_home)
                results_home["predict_home"] = y_pred_home


            else:
                predicted = gbm.predict(X_test, num_iteration=gbm.best_iteration)
                y_pred= np.argmax(predicted, axis=1)  # 最尤と判断したクラスの値にする
                results[col] = y_pred
    
    return results, results_home


"""
print("done")
print(results["predict_0"])
print("--------------------------")
print(results["predict_1"])
print("--------------------------")
print(results["predict_2"])
print("--------------------------")
print(results_home["predict_home"])
"""

if __name__ == "__main__":
    path_to_df_file = "create_model/data/df.pickle"
    #num_boost_round引数は勾配ブースティングのイテレーションの回数
    path_to_models_dir = "create_model/trained_models/"
    train(path_to_df_file, path_to_models_dir)