# ref: https://towardsdatascience.com/deploying-a-machine-learning-model-as-a-rest-api-4a03b865c166
# ref2: https://towardsdatascience.com/a-flask-api-for-serving-scikit-learn-models-c8bcdaa41daa
# ref3: https://github.com/amirziai/sklearnflask
# ref4: https://www.lynda.com/Flask-tutorials/Web-API-Development-Flask/
import sys
import os
import shutil
import time
import traceback

from flask import Flask, jsonify
from sklearn.externals import joblib
import pandas as pd

app = Flask(__name__)

# load the model
model = joblib.load('../modeling/rf_clf.pkl')


@app.route('/predict', methods=['POST'])
def predict():
    print("predicitng with a Random Forest classifier")
    json_of_interest = request.json
    query = pd.get_dummies(pd.DataFrame(json_of_interest))

    print(query.shape)

if __name__ == "__main__":
    app.run(debug=True)