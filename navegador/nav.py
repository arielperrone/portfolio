from flask import Flask
app = Flask(__name__)
@app.route("/")
    def home():
        return "navegador"
if__name__=='__main__':
