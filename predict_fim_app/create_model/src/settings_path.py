import os
path_to_df_file = os.environ.get("FIM_Data_File", "predict_fim_app/create_model/data/df.pickle")
path_to_models_dir = os.environ.get("Models_Dir", "predict_fim_app/create_model/trained_models/")
path_to_test_data_json = os.environ.get("Test_Data", "predict_fim_app/create_model/data/test_data/test.json")
path_to_materials_file = os.environ.get("Materials_File", "predict_fim_app/create_model/src/materials.py")