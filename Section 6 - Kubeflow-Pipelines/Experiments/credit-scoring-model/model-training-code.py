import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, precision_score, recall_score, roc_auc_score, accuracy_score
from xgboost import XGBClassifier
from google.cloud import storage

storage_client = storage.Client()
bucket = storage_client.bucket("sid-kubeflow-v1")

def purpose_encode(x):
    return {
        "Consumer Goods": 1,
        "Vehicle": 2,
        "Tuition": 3,
        "Business": 4,
        "Repairs": 5
    }.get(x, 0)

def other_parties_encode(x):
    return {"Guarantor": 1, "Co-Applicant": 2}.get(x, 0)

def qualification_encode(x):
    return {"unskilled": 1, "skilled": 2, "highly skilled": 3}.get(x, 0)

def credit_standing_encode(x):
    return 1 if x == "good" else 0

def assets_encode(x):
    return {"Vehicle": 1, "Investments": 2, "Home": 3}.get(x, 0)

def housing_encode(x):
    return {"rent": 1, "own": 2}.get(x, 0)

def marital_status_encode(x):
    return {"Married": 1, "Single": 2}.get(x, 0)

def other_payment_plans_encode(x):
    return {"bank": 1, "stores": 2}.get(x, 0)

def sex_encode(x):
    return 1 if x == "M" else 0

def credit_score_decode(x):
    return "Approved" if x == 1 else "Denied"

def preprocess_data(df):
    encoding_functions = {
        "PURPOSE": purpose_encode,
        "OTHER_PARTIES": other_parties_encode,
        "QUALIFICATION": qualification_encode,
        "CREDIT_STANDING": credit_standing_encode,
        "ASSETS": assets_encode,
        "HOUSING": housing_encode,
        "MARITAL_STATUS": marital_status_encode,
        "OTHER_PAYMENT_PLANS": other_payment_plans_encode,
        "SEX": sex_encode
    }

    for column, func in encoding_functions.items():
        df[f"{column}_CODE"] = df[column].apply(func)

    columns_to_drop = list(encoding_functions.keys())
    return df.drop(columns=columns_to_drop)

def split_data(df):
    return train_test_split(df.drop('CREDIT_STANDING_CODE', axis=1), 
                            df['CREDIT_STANDING_CODE'], test_size=0.30)

def train_model(X_train, y_train, max_depth, learning_rate, n_estimators):    
    model = XGBClassifier(
        max_depth=max_depth,
        learning_rate=learning_rate,
        n_estimators=n_estimators,
        random_state=42,
        use_label_encoder=False
    )    
    model.fit(X_train, y_train)
    return model

def save_model_artifact(pipeline):
    artifact_name = 'model.bst'
    pipeline.save_model(artifact_name)
    model_artifact = bucket.blob(f'credit-scoring/artifacts/{artifact_name}')
    model_artifact.upload_from_filename(artifact_name)

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    return (
        accuracy_score(y_test, y_pred),
        precision_score(y_test, y_pred),
        recall_score(y_test, y_pred)
    )

# Main execution
input_file = "gs://sid-kubeflow-v1/credit-scoring/credit_files.csv"
credit_df = pd.read_csv(input_file)
credit_df = preprocess_data(credit_df)

X_train, X_test, y_train, y_test = split_data(credit_df)

max_depth = 5
learning_rate = 0.2
n_estimators = 40
pipeline = train_model(X_train, y_train, max_depth, learning_rate, n_estimators)

accuracy, precision, recall = evaluate_model(pipeline, X_test, y_test)

if accuracy > 0.5 and precision > 0.5:
    save_model_artifact(pipeline)
    model_validation = "true"
else:
    model_validation = "false"
