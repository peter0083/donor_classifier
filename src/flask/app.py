# ref: https://towardsdatascience.com/deploying-a-machine-learning-model-as-a-rest-api-4a03b865c166
# ref2: https://towardsdatascience.com/a-flask-api-for-serving-scikit-learn-models-c8bcdaa41daa
# ref3: https://github.com/amirziai/sklearnflask
import sys
import os
import shutil
import time
import traceback

from flask import Flask, jsonify
from sklearn.externals import joblib
import pandas as pd

app = Flask(__name__)

