import json
import os
import matplotlib.pyplot as plt
import numpy as np
import pickle
import pandas as pd
import plotly.express as px
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from . import forms, models
from .forms import CareForm
from .materials_cp import column_afters, column_current, input_columns, sum_1M, sum_2M, sum_3M, fim_motor_item

# pathが難しい。 materials_cpを作成し読み込む。使用したい関数は下記に作成（materials_cpに関数を描いても良いカモ）

prediction_columns = column_afters
column_current = column_current
almost_prediction_columns = list(prediction_columns[1]) + list(prediction_columns[2]) + list(prediction_columns[3])

path_to_models_dir = "predict_fim_app/create_model/trained_models/"





def predict(request):
    context = {"form":CareForm()}  
    return render(request, "predict_fim_app/predict.html", context)



def result(request):
    #post dataをdbに保存(modelで作成した name=db *fim_data.sq;ite3ではない)
    form = forms.CareForm(request.POST or None)
    if form.is_valid():
        models.Predict_Fim_App.objects.create(**form.cleaned_data)
        
    #1)リクエストdataを全て受け取る 
    data_dict = request.POST
    input_dict = pd.DataFrame.from_dict(data_dict, orient='index').T
    input_dict = input_dict[input_columns]
    input_dict = input_dict.astype('int64')


    # 学習は0-6でしているため合わせる
    input_dict[column_current] = input_dict[column_current] - 1

    results={}
    results_home={}

    for length_value in range(len(prediction_columns)): #4

        for col in prediction_columns[length_value]:
            name =  col + "_LGBM.pkl"
            filename = os.path.join(path_to_models_dir, name)

            with open(filename, 'rb') as web:
                loaded_model = pickle.load(web)
    

            
            #テストデータの予測 length_value==0 は 自宅復帰を予測
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
    
    # FIM合計と項目ごとの推移を抽出
    output_df = pd.DataFrame.from_dict(results, orient='index').T
    output_df[almost_prediction_columns] = output_df[almost_prediction_columns] + 1
    
    df_sum_score, df_score, fim_profit = _acurate_sum(output_df, input_dict)

    #グラフの作成とそれをHTMLとして取得
    import plotly.express as px
    from plotly.offline import plot
    import plotly.figure_factory as ff
    df_graph = pd.DataFrame(np.array(df_sum_score), index=["現在", "１ヶ月後予測", "2ヶ月後予測", "3ヶ月後予測"], columns=["FIM合計点数"])
    fig_graph = px.line(df_graph,x=df_graph.index, y="FIM合計点数",  title='FIM合計点の予測', hover_name=df_graph.index)
    fig_graph_html = plot(fig_graph, output_type='div', include_plotlyjs=False)

    fig_table = ff.create_table(df_score, height_constant=30,index=True,index_title='FIM 項目')
    #fig_table.layout.width=400
    fig_table_html = plot(fig_table, output_type='div', include_plotlyjs=False)



    #template用に加工
    discharge = round(results_home["predict_home"][0] *100)

    present = int(df_sum_score[0])
    after_1M = int(df_sum_score[1])
    after_2M = int(df_sum_score[2])
    after_3M = int(df_sum_score[3])

    
    template = loader.get_template("predict_fim_app/result.html")
    context={
        "discharge": discharge,
        "present": present,
        "after_1M": after_1M,
        "after_2M": after_2M,
        "after_3M": after_3M,
        "df_score": df_score,
        'fig_graph_html': fig_graph_html,
        'fig_table_html': fig_table_html,
        'fim_profit': fim_profit
            }

    
    return render(request, "predict_fim_app/result.html", context)
    

def _acurate_sum(output_df, input_dict):
    # それぞれのカラムのデータfラームを抽出
    score_0M = input_dict[column_current]
    score_1M = output_df[sum_1M]
    score_2M = output_df[sum_2M]
    score_3M = output_df[sum_3M]

    #column名を揃える
    score_1M.columns = column_current
    score_2M.columns = column_current
    score_3M.columns = column_current


    #合計を計算
    sum_0M_score = score_0M.sum(axis=1)
    sum_1M_score = score_1M.sum(axis=1)
    sum_2M_score = score_2M.sum(axis=1)
    sum_3M_score = score_3M.sum(axis=1)

    # 合計点数と各項目をdataframe化
    df_sum_score = [sum_0M_score, sum_1M_score,sum_2M_score,sum_3M_score]
    df_score = pd.concat([score_0M, score_1M, score_2M, score_3M]).T
    df_score.columns = ["現在", "１ヶ月後", "2ヶ月後", "3ヶ月後"]

    # FIM利得計算
    fim_enter = score_0M[fim_motor_item].sum(axis=1)
    fim_discharge = score_3M[fim_motor_item].sum(axis=1)
    fim_profit = fim_discharge - fim_enter
    
    return df_sum_score, df_score, fim_profit[0]


