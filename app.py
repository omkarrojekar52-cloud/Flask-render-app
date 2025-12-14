from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Omkar 🚀 Flask app is live on Render!"
