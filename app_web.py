# ref: https://towardsdatascience.com/deploying-a-machine-learning-model-as-a-rest-api-4a03b865c166
# ref2: https://towardsdatascience.com/a-flask-api-for-serving-scikit-learn-models-c8bcdaa41daa
# ref3: https://github.com/amirziai/sklearnflask
# ref4: https://www.lynda.com/Flask-tutorials/Web-API-Development-Flask/
import sys
import os
import shutil
import time
import traceback

from flask import Flask, request, jsonify
from sklearn.externals import joblib
import pandas as pd
from pandas.io.json import json_normalize

app = Flask(__name__)

# load the model
model = joblib.load('rf_clf_web.pkl')

# load the training data
train_df_template = pd.read_csv('train_complete_web.csv', index_col= 0)

# get dummy columns from data template
dummy_cols = ["workclass", "education",
             "marital_stat", "occupation",
             "relationship", "race",
             "sex", "native_country"]

train_df_template_with_dummies = pd.get_dummies(train_df_template, columns= dummy_cols)

train_df_template_with_dummies_no_label = train_df_template_with_dummies.drop(['label'], axis=1)

# save the column names
model_columns = list(train_df_template_with_dummies_no_label.columns)

@app.route('/predict', methods=['POST'])
def predict():
    jsonData = request.json
    client_df = pd.get_dummies(pd.DataFrame.from_dict(json_normalize(jsonData), orient='columns'))
    # ref: https://github.com/amirziai/sklearnflask/issues/3
    query = client_df.reindex(columns=model_columns, fill_value=0)
    
    # ref: https://stackoverflow.com/questions/26646362/numpy-array-is-not-json-serializable
    prediction = model.predict(query).tolist()

    return jsonify({
        "prediction": prediction
    })
    

if __name__ == "__main__":
    app.run(debug=True)