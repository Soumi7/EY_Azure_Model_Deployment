from flask import Flask, request, jsonify, render_template, url_for
import tensorflow as tf
import os
import numpy as np
app = Flask(__name__)


model = tf.keras.models.load_model('saved_model/ey_model')



@app.route('/')
def home():
    return 'Hello World'

@app.route('/predict_api', methods=["POST"])
def list_post():
    json_body = request.get_json()
    print(json_body[0])
    #print(json_body[1])

    predictions = model.predict(json_body).argmax(axis=-1)
    print(predictions)
    #predictions = 2 * json_body[0]    
    # * this is show query params needs to parsed manually
    #print((request.query_string).decode("utf-8"))
    #l={'predictions':list(predictions)}
    predictions = list(predictions)
    for i in range(0,len(predictions)) :
        predictions[i] = int(predictions[i])      

    return jsonify(results = predictions)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0',port=80)

