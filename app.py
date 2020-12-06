from flask import Flask, request, jsonify, render_template, url_for
import tensorflow as tf
import os
import numpy as np
from bert.tokenization.bert_tokenization import FullTokenizer
#from tensorflow import keras
bert_ckpt_dir=""
tokenizer = FullTokenizer(vocab_file="vocab.txt")

app = Flask(__name__)

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

for text, label in zip(sentences, predictions):
  print("text:", text, "\nintent:", classes[label])
  print()

@app.route('/')
def home():
    return 'Hello World'

'''
    
@app.route('/predict_api','<list(str):pred_token_ids>',methods=['POST','GET'])
def predict_api():
    
    #For direct API calls trought request
    
    predictions = model.predict(pred_token_ids).argmax(axis=-1)
    return jsonify({'predictions': predictions})
'''

if __name__ == '__main__':
    app.run(debug=True)
