import pandas as pd
from build_model import rmse

y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]


def test_rmse():
    assert rmse(y_true, y_pred) == 0.6123724356957945
    # assert rmse(y_true, y_pred) == 1


def test_data_leak_in_testdata():
    df_train = pd.read_csv("data/nyc_taxi_dataset_train.csv")
    df_valid = pd.read_csv("data/nyc_taxi_dataset_valid.csv")

    concat_df = pd.concat([df_train, df_valid])
    concat_df.drop_duplicates(inplace=True)

    assert concat_df.shape[0] == df_train.shape[0] + df_valid.shape[0]
