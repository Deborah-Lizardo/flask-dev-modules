from flask import Flask, render_template, request, redirect, url_for

from login import login
from sensors import sensors_bp
from actuators import actuators_bp

app = Flask(__name__)
app.register_blueprint(login, url_prefix='/')
app.register_blueprint(sensors_bp, url_prefix='/')
app.register_blueprint(actuators_bp, url_prefix='/')

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/home')
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
