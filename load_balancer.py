from flask import Flask, request, jsonify

app = Flask(__name__)

seed = "0.0"

@app.route("/", methods = ['POST', 'GET'])
def hello_world():
    global seed

    if request.method == 'POST':
        data = request.get_json()
        seed = data["num"]
        return jsonify(success=True)
    else:
        return jsonify(seed=seed)

app.run(host='0.0.0.0',port=5003)