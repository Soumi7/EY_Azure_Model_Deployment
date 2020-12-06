from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/lists', methods=["POST"])
def list_post():
    json_body = request.get_json()
    print(json_body)
    
    # * this is show query params needs to parsed manually
    print((request.query_string).decode("utf-8"))

    
    return {
        "resp": [1, 2, 3]
    }

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0',port=5000)