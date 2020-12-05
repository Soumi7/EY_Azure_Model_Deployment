from flask import Flask, request, jsonify, render_template, url_for
import tensorflow as tf
from tensorflow import keras

app = Flask(__name__)
model = tf.keras.models.load_model('./saved_model/ey_model')

@app.route('/')
def home():
    #return 'Hello World'
    return render_template('home.html')
    #return render_template('index.html')
    
@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    
    data = request.form.getlist('data[]')
    predictions = model.predict(pred_token_ids).argmax(axis=-1)
    return jsonify(predictions)


if __name__ == '__main__':
    app.run(debug=True)
