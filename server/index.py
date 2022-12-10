from flask import Flask, jsonify,request

app = Flask(__name__)

block= []

# @app.route("/")
# def hello_world():
#     return "Hello, World!"

@app.route('/data/', methods=['GET'])
def get_blockchain():
    return jsonify(block)


@app.route('/data/', methods=['POST'])
def add_data_to_blockchain():
    data=request.get_json()
    block.append(data)
    return '', 204
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)