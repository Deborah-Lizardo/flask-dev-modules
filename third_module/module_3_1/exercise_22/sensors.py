from flask import Blueprint, render_template, request

sensors_bp = Blueprint('sensors', __name__, template_folder="templates")

sensors = {'temperature':23, 'humidity':22, 'luminosity':10}

@sensors_bp.route('/sensors')
def list_sensors():
    return render_template("sensors.html", sensors=sensors)

@sensors_bp.route('/register_sensor', methods=['GET', 'POST'])
def register_sensor():
    global sensors
    if request.method == 'POST':
        sensor_name = request.form['name']
        sensor_value = request.form['value']
        sensors[sensor_name] = int(sensor_value)
        return render_template("sensors.html", sensors=sensors)
    else:
        return render_template("register_sensor.html")
    

@sensors_bp.route('/remove_sensor')
def del_sensor():
    return render_template("remove_sensor.html", sensors=sensors)


@sensors_bp.route('/del_sensor', methods=['GET', 'POST'])
def remove_sensor():
    global sensors
    if request.method == 'POST':
        sensor = request.form['name']
    else:
        sensor = request.args.get('name', None)

    if sensor in sensors:
        sensors.pop(sensor)
    return render_template("sensors.html", sensors=sensors)

