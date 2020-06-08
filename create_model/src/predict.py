import os
import numpy as np
import pandas as pd
import lightgbm as lgb
import pickle
import json

import settings_path as s
import materials
import utilities as u



#docker image前のテスト：「POSTする値」を想定し、jsonファイルを作り、それを読み込んでテスト。テストするときはコメントアウト外す。
#f = open('test.json', 'r')
#data_dict = json.load(f)
#path_to_models_dir  = s.path_to_models_dir 

path_to_test_data_json = s.path_to_test_data_json
path_to_models_dir = s.path_to_models_dir


prediction_columns = materials.column_afters   # 4
discharge = list(prediction_columns[0])
almost_prediction_columns = list(prediction_columns[1]) + list(prediction_columns[2]) + list(prediction_columns[3])
all_prediction_columns = discharge + almost_prediction_columns 

column_current = materials.column_current

f = open(path_to_test_data_json, 'r')
data_dict = json.load(f)

print("準備ok")


def predict(path_to_test_data_json,path_to_models_dir ):    
    results={}
    results_home={}

    for length_value in range(len(prediction_columns)):

        for col in prediction_columns[length_value]:
            name =  col + "_LGBM.pkl"
            filename = os.path.join(path_to_models_dir, name)

            with open(filename, 'rb') as web:
                loaded_model = pickle.load(web)
    
            input_dict = pd.DataFrame.from_dict(data_dict, orient='index').T
            input_dict = input_dict.drop("id", axis=1)

            # 学習は0-6でしているため合わせる
            input_dict[column_current] = input_dict[column_current] - 1

            
             #テストデータの予測
            if length_value == 0:
                predicted_home = loaded_model.predict(input_dict)
            
                y_pred_home = []
                for x in predicted_home:
                    y_pred_home.append(np.round(x))

                y_pred_home = np.array(y_pred_home)
                results_home["predict_home"] = [predicted_home[0], y_pred_home[0]]


            else:
                predicted = loaded_model.predict(input_dict)
                y_pred= np.argmax(predicted, axis=1)  # 最尤と判断したクラスの値にする
                results[col] = y_pred[0]
           
    output_df = pd.DataFrame.from_dict(results, orient='index').T
    output_df[almost_prediction_columns] = output_df[almost_prediction_columns] + 1

    df_sum_score, df_score = u.acurate_sum(output_df)

    #print(results_home)
 
    return results_home, df_sum_score, df_score
    
 


    """print("1ヶ月後")
    print(output_df[prediction_columns[1]])
    print("--------------------------")
    print("２ヶ月後")
    print(output_df[prediction_columns[2]])
    
    print("--------------------------")
    print("３ヶ月後")
    print(output_df[prediction_columns[3]])
    print("--------------------------")
    print(results_home["predict_home"])
    #print(output_df)
    #print(results_home)"""
    


if __name__ == "__main__":
    predict(path_to_test_data_json,path_to_models_dir )
