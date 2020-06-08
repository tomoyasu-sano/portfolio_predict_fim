import os
path_to_df_file = os.environ.get("FIM_Data_File", "./create_model/data/df.pickle")
path_to_models_dir = os.environ.get("Models_dir", "./create_model/trained_models/")
path_to_test_data_json = os.environ.get("Test_data", "./create_model/data/test_data/test.json")