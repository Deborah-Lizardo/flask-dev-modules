from flask import Flask, render_template, request, redirect, url_for

from login import login
from sensors import sensors_bp

app = Flask(__name__)
app.register_blueprint(login, url_prefix='/')
app.register_blueprint(sensors_bp, url_prefix='/')

actuators = {'lamp': 1, 'serv motor': 122}

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/actuator')
def actuator():
    return render_template("actuators.html", actuators=actuators)

@app.route('/register_actuator')
def register_actuator():
    return render_template("register_actuators.html")

@app.route('/add_actuator', methods=['GET', 'POST'])
def add_actuator():
    global actuators
    if request.method == 'POST':
        actuator_name = request.form['actuator']
        actuator_value = request.form['value']
        if actuator_name in actuators:
            return f'<h1>Actuator "{actuator_name}" already exists!</h1><a href="/register_actuator">Go back</a>'
        else:
            actuators[actuator_name] = int(actuator_value)
            return render_template("actuators.html", actuators=actuators)
    else:
        return render_template("register_actuators.html")

@app.route('/list_actuators')
def list_actuators():
    return render_template("actuators.html", actuators=actuators)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
