from flask import Flask, request, jsonify, render_template, url_for
import tensorflow as tf
import os
import numpy as np
import json
app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World'


    
@app.route('/predict_api',methods=['POST'])
def predict_api():
    json_body = request.get_json(force=True)
    print(json_body)
    print((request.query_string).decode("utf-8"))
    predictions = [1,0,0,1]

    return jsonify({'predictions': predictions})


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0',port=80)
