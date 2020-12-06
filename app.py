from flask import Flask, request, jsonify, render_template, url_for
import tensorflow as tf
import os
import numpy as np
#from tensorflow import keras
#import bert
#from bert.tokenization.bert_tokenization import FullTokenizer

app = Flask(__name__)

'''

bert_ckpt_dir=""
tokenizer = FullTokenizer(vocab_file="vocab.txt")


sentences = [
  "we are studying for exam", "i dont know"
]

pred_tokens = map(tokenizer.tokenize, sentences)
pred_tokens = map(lambda tok: ["[CLS]"] + tok + ["[SEP]"], pred_tokens)
pred_token_ids = list(map(tokenizer.convert_tokens_to_ids, pred_tokens))

pred_token_ids = map(lambda tids: tids +[0]*(128-len(tids)),pred_token_ids)
pred_token_ids = np.array(list(pred_token_ids))
print(pred_token_ids)
model = tf.keras.models.load_model('saved_model/ey_model')

predictions = model.predict(pred_token_ids).argmax(axis=-1)

classes = ['Financial Reports', 'Case Study', 'Coding Guidelines']

for text, label in zip(sentences, predictions):
  print("text:", text, "\nintent:", classes[label])
  print()

'''
@app.route('/')
def home():
    return 'Hello World'


    
@app.route('/predict_api',methods=['POST','GET'])
def predict_api():
    request_json = request.get_json()
    sentences = request_json.get('sentences')
    for i in sentences:
      print(i)

    predictions = [1,0,0,1]

    return jsonify({'predictions': predictions})


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0',port=80)
