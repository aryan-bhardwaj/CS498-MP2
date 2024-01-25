from flask import Flask, request, jsonify
import socket, subprocess

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def hello_world():
    global seed

    if request.method == 'POST':
        subprocess.Popen(['python3', 'stress_cpu.py'])
        return "Running stress_cpu.py"
    else:
        return socket.gethostbyname(socket.gethostname())

app.run(host='0.0.0.0',port=5003)