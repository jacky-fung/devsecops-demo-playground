from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello DevSecOps!"

@app.route("/run")
def run():
    cmd = request.args.get("cmd")
    return subprocess.getoutput(cmd)

if __name__ == "__main__":
    app.run(debug=True)