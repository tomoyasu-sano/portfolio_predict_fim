#results ={'meal_after_1M': 1, 'hygienic_after_1M': 1, 'wipingClean_after_1M': 1, 'upperBodyDressing_after_1M': 1, 'lowerBodyDressing_after_1M': 1, 'toiletAction_after_1M': 1, 'urinationControl_after_1M': 1, 'defecationControl_after_1M': 1, 'bedsChairsWheelchairs_after_1M': 1, 'toilet_after_1M': 1, 'bathtubShower_after_1M': 1, 'walkingWheelchair_after_1M': 1, 'stairs_after_1M': 1, 'understanding_after_1M': 1, 'expression_after_1M': 1, 'socialCommunication_after_1M': 1, 'problemSolving_after_1M': 1, 'memory_after_1M': 1, 'meal_after_2M': 3, 'hygienic_after_2M': 3, 'wipingClean_after_2M': 3, 'upperBodyDressing_after_2M': 3, 'lowerBodyDressing_after_2M': 3, 'toiletAction_after_2M': 3, 'urinationControl_after_2M': 3, 'defecationControl_after_2M': 3, 'bedsChairsWheelchairs_after_2M': 3, 'toilet_after_2M': 3, 'bathtubShower_after_2M': 3, 'walkingWheelchair_after_2M': 3, 'stairs_after_2M': 3, 'understanding_after_2M': 3, 'expression_after_2M': 3, 'socialCommunication_after_2M': 3, 'problemSolving_after_2M': 3, 'memory_after_2M': 3, 'meal_after_3M': 3, 'hygienic_after_3M': 3, 'wipingClean_after_3M': 3, 'upperBodyDressing_after_3M': 3, 'lowerBodyDressing_after_3M': 3, 'toiletAction_after_3M': 3, 'urinationControl_after_3M': 3, 'defecationControl_after_3M': 3, 'bedsChairsWheelchairs_after_3M': 3, 'toilet_after_3M': 3, 'bathtubShower_after_3M': 3, 'walkingWheelchair_after_3M': 3, 'stairs_after_3M': 3, 'understanding_after_3M': 3, 'expression_after_3M': 3, 'socialCommunication_after_3M': 3, 'problemSolving_after_3M': 3, 'memory_after_3M': 3}
#results_home = {'predict_home': [0.06937913507760483, 0.0]}


import json
import pandas as pd

from materials import sum_1M, sum_2M, sum_3M, column_current
from predict import predict
import settings_path as s
from settings_path import path_to_test_data_json


f = open(path_to_test_data_json, 'r')
data_dict = json.load(f)

def acurate_sum(output_df, data_dict):

#path_to_test_data_json = s.path_to_test_data_json
#path_to_models_dir = s.path_to_models_dir

#output_df, results_home = predict(path_to_test_data_json, path_to_models_dir)



    score_0M = []
    score_1M = []
    score_2M = []
    score_3M = []

    for k , v in data_dict.items():
        if k in column_current:
            score_0M.append(v)

    for k, v in output_df.items():
        if k in sum_1M:
            score_1M.append(v)
        elif k in sum_2M:
            score_2M.append(v)
        else:
            score_3M.append(v)
    

    sum_0M_score = sum(score_0M)
    sum_1M_score =sum(score_1M)
    sum_2M_score = sum(score_2M)
    sum_3M_score = sum(score_3M)

    df_sum_score = pd.Series([sum_0M_score, sum_1M_score,sum_2M_score,sum_3M_score])

    df_score = pd.DataFrame([score_0M, score_1M, score_2M, score_3M],index=["現在", "１ヶ月後予測", "2ヶ月後予測", "3ヶ月後予測"],columns=column_current).T

    return df_sum_score, df_score