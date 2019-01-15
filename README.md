# donor_classifier
practice deploying a ML model

Goal: Assuming that a charity realizes that people who make more than $50k/yr are more likely to donate and this charity organization wishes to identify potential donors, predict whether income exceeds $50K/yr based on census data. 

Data source: https://archive.ics.uci.edu/ml/datasets/Adult



### 1. Explorartory data analysis
- documented [here](https://github.com/peter0083/donor_classifier/blob/master/doc/EDA.md)

### 2. ML model building
- traditional ML models documented [here](https://github.com/peter0083/donor_classifier/blob/master/src/modeling/ml_model.ipynb)
- neural net model documented [here](https://github.com/peter0083/donor_classifier/blob/master/src/modeling/neural_net.ipynb)

### 3. ML model as a RESTful API
- [actual server app](https://github.com/peter0083/donor_classifier/blob/master/app_web.py)
- the API is deployed on Heroku (https://donorclf.herokuapp.com/predict)

Sending a request to the API:

**example:**

We can send a request to https://donorclf.herokuapp.com/predict and request for a prediction for the following donor:

| age            | 39            |
|----------------|---------------|
| workclass      | State-gov     |
| fnlwgt         | 77516         |
| education      | Bachelors     |
| education_num  | 13            |
| marital_stat   | Never-married |
| occupation     | Adm-clerical  |
| relationship   | Not-in-family |
| race           | White         |
| sex            | Male          |
| capital_gain   | 2174          |
| capital_loss   | 0             |
| hr_per_wk      | 40            |
| native_country | United-States |

The request should be sent in `json` format

```json
{"age":39,"workclass":" State-gov","fnlwgt":77516,"education":" Bachelors","education_num":13,"marital_stat":" Never-married","occupation":" Adm-clerical","relationship":" Not-in-family","race":" White","sex":" Male","capital_gain":2174,"capital_loss":0,"hr_per_wk":40,"native_country":" United-States"}
```

The API should return a prediction in `json` format

```json
{
    "prediction": [
        0
    ]
}
```

If the prediction is **0**, then the model classifies the donor as a donor that makes **LESS** than $50k annually.

If the prediction is **1**, then the model classifies the donor as a donor that makes **MORE** than $50k annually.

Next step:
1. I left some sanity check code chunks in the EDA and modelling parts. I haven't been able to rewrite them as proper unit tests yet.
2. The API needs a more through testing as well. 
3. Input authentication has not be implemented yet.
