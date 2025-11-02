from flask import Flask, render_template, request
app= Flask( __name__ )

users = {'user1': '1234','user2': '1234'}
actuators = {'temperature':23, 'humidity':22, 'luminosity':10}
actuators = {'lamp': 1, 'serv motor': 122}

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/validated_user', methods=['POST', 'GET'])
def validated_user():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        print(user, password)
        if user in users and users[user] == password:
            return render_template('home.html')
        else:
            return '<h1>invalid credentials!</h1>'
    else:
        return render_template('login.html')

@app.route('/register_user')
def register_user():
    return render_template("register_user.html")

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    global users
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
    else:
        user = request.args.get('user', None)
        password = request.args.get('password', None)
    users[user] = password
    return render_template("users.html", devices=users)

@app.route('/list_users')
def list_users():
    global users
    return render_template("users.html", devices=users)


@app.route('/remove_user')
def remove_user():
    return render_template("remove_user.html", devices=users)


@app.route('/del_user', methods=['GET', 'POST'])
def del_user():
    global users
    if request.method == 'POST':
        user = request.form['user']
    else:
        user = request.args.get('user', None)

    if user in users:
        users.pop(user)

    return render_template("users.html", devices=users)


@app.route('/actuator')
def actuator():
    actuators = {'lamp': 1, 'serv motor': 122}
    return render_template("actuators.html", actuators=actuators)

@app.route('/register_actuator')
def register_actuator():
    return render_template("register_actuators.html")

@app.route('/sensor')
def sensor():
    sensors = {'temperature': 23, 'humidity': 22, 'luminosity': 10}
    return render_template("sensors.html", sensors=sensors)

@app.route('/register_sensor')
def register_sensor():
    return render_template("register_sensor.html")

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

@app.route('/add_sensor', methods=['GET', 'POST'])
def add_sensor():
    global actuators
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


@app.route('/list_sensors')
def list_sensors():
    return render_template("sensors.html", sensors=actuators)

@app.route('/remove_sensor')
def remove_sensor():
    return render_template("remove_sensor.html", devices=actuators)

@app.route('/del_sensor', methods=['GET', 'POST'])
def del_sensor():
    global actuators
    if request.method == 'POST':
        sensor = request.form['sensor']
    else:
        sensor = request.args.get('sensor', None)

    if sensor in sensors:
        sensors.pop(sensor)

    return render_template("sensors.html", devices=sensors)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
