import json
import numpy as np
import pandas as pd
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from .forms import CareForm

from create_model.src import settings_path
from create_model.src import utilities

path_to_models_dir = settings_path.path_to_models_dir
materials = settings_path.path_to_materials_file
prediction_columns = materials.column_afters   # 4
discharge = list(prediction_columns[0])
almost_prediction_columns = list(prediction_columns[1]) + list(prediction_columns[2]) + list(prediction_columns[3])
all_prediction_columns = discharge + almost_prediction_columns 
column_current = materials.column_current

###　整理する。予測するページと結果を返すページ　
### AIのモデルを読み込み計算
### デザイン
def predict(request):
    context = {"form":CareForm()}  
    return render(request, "predict_fim_app/predict.html", context)


def result(request):
    #1)リクエストdataを全て受け取る 
    data_dict = request.POST
    input_dict = pd.DataFrame.from_dict(data_dict, orient='index').T

    results={}
    results_home={}

    for length_value in range(len(prediction_columns)):

        for col in prediction_columns[length_value]:
            name =  col + "_LGBM.pkl"
            filename = os.path.join(path_to_models_dir, name)

            with open(filename, 'rb') as web:
                loaded_model = pickle.load(web)
    
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

    df_sum_score, df_score = utilities.acurate_sum(output_df)

  









    template = loader.get_template("predict_fim_app/result.html")
    context={
        "value": value
    }
    #context={
     #   "predicted": predicted,
      #  "percentage":percentage
    #}
    return render(request, "predict_fim_app/result.html", context)
    
    #return render(request, "predict_fim_app/result.html")


    


"""
def index(request):
    return render(request, "predict_fim_app/dog.html")
 """   