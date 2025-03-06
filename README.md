# flask-cloud-app from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>ABDIFATAH SOANE AHMED</h1><p>Registration Number: 23/07836 BSD</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
