from flask import Flask, render_template, request, redirect, url_for
from login import login

app = Flask(__name__)
app.register_blueprint(login, url_prefix='/')

users = {'user1': '1234', 'user2': '1234'}
actuators = {'temperature': 23, 'humidity': 22, 'luminosity': 10}
actuators = {'lamp': 1, 'serv motor': 122}

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/home')
def home():
    return render_template("home.html")
@app.route('/actuators')
def list_actuators():
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

@app.route('/sensor')
def sensor():
    return render_template("sensors.html", sensors=actuators)

@app.route('/register_sensor')
def register_sensor():
    return render_template("register_sensor.html")

@app.route('/add_sensor', methods=['GET', 'POST'])
def add_sensor():
    global sensors
    if request.method == 'POST':
        sensor_name = request.form['sensor']
        sensor_value = request.form['value']
        if sensor_name in sensors:
            return f'<h1>Sensor "{sensor_name}" already exists!</h1><a href="/register_sensor">Go back</a>'
        else:
            sensors[sensor_name] = int(sensor_value)
            return render_template("sensors.html", sensors=sensors)
    else:
        return render_template("register_sensor.html")

@app.route('/sensors')
def list_sensors():
    return render_template("sensors.html", sensors=sensors)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
