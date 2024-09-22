import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from google.cloud import storage
from joblib import dump
from sklearn.pipeline import make_pipeline
import hypertune
import argparse
import sys

def load_data(filename):
    try:
        df = pd.read_csv(filename)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        sys.exit(1)

def preprocess_data(df):
    df = df.rename(columns={'weathersit':'weather', 'yr':'year', 'mnth':'month',
                            'hr':'hour', 'hum':'humidity', 'cnt':'count'})
    df = df.drop(columns=['instant', 'dteday', 'year'])
    cols = ['season', 'month', 'hour', 'holiday', 'weekday', 'workingday', 'weather']
    for col in cols:
        df[col] = df[col].astype('category')
    df['count'] = np.log(df['count'])
    df_oh = df.copy()
    for col in cols:
        df_oh = one_hot_encoding(df_oh, col)
    X = df_oh.drop(columns=['atemp', 'windspeed', 'casual', 'registered', 'count'], axis=1)
    y = df_oh['count']
    return X, y

def one_hot_encoding(data, column):
    data = pd.concat([data, pd.get_dummies(data[column], prefix=column, drop_first=True)], axis=1)
    data = data.drop([column], axis=1)
    return data

def train_model(x_train, y_train, n_estimators):
    model = RandomForestRegressor(max_depth=None, n_estimators=n_estimators)
    pipeline = make_pipeline(model)
    pipeline.fit(x_train, y_train)
    return pipeline

def main(args):
    filename = 'gs://udemy-gcp-mlops/bikeshare-model/hour.csv'
    df = load_data(filename)
    X, y = preprocess_data(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    pipeline = train_model(X_train, y_train, args.n_estimators)
    y_pred = pipeline.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    hpt = hypertune.HyperTune()
    hpt.report_hyperparameter_tuning_metric(
        hyperparameter_metric_tag='rmse',
        metric_value=rmse,
        global_step=1000
    )
    print('RMSE:', rmse)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_estimators", dest="n_estimators", default=20, type=int, help="Number of estimators")
    args = parser.parse_args()
    main(args)
