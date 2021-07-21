import os
import json
import time
import math
from flask import Flask, request, jsonify
from flask_rest4 import Api, Resource
import sklearn
import tensorflow as tf
from tensorflow import keras
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

np.random.seed(42)
tf.random.set_seed(42)

app = Flask(__name__)
api = Api(app)
model = keras.models.load_model('model.h5')
num_pipeline = Pipeline([
    ('std_scaler', StandardScaler())
])


@api.route("/")
def lstm():
	input_num = np.array(request.json['close']).reshape(-1, 1)
	input = num_pipeline.fit_transform(input_num)
	input_array = [input]
	input_array = np.array(input_array)
	predicted = model.predict(input_array)
	final_prediction = num_pipeline.inverse_transform(predicted)
	print(final_prediction[:, -1][..., np.newaxis])
	return final_prediction[0][-1][0]


if __name__ == '__main__':
    app.run(debug=True)
