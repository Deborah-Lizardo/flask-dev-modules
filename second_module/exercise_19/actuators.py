from flask import Blueprint, render_template, request
actuators_bp = Blueprint('actuators', __name__, template_folder="templates")

actuators = {'lamp':1, 'serv motor':122}

@actuators_bp.route('/actuators')
def actuator():
    return render_template("actuators.html", actuators=actuators)

@actuators_bp.route('/register_actuator')
def register_actuator():
    return render_template("register_actuators.html")

@actuators_bp.route('/add_actuator', methods=['GET', 'POST'])
def add_actuator():
    global actuators
    if request.method == 'POST':
        actuator_name = request.form['actuator']
        actuator_value = request.form['value']
        actuators[actuator_name] = int(actuator_value)
        return render_template("actuators.html", actuators=actuators)
    else:
        return render_template("register_actuators.html")

@actuators_bp.route('/list_actuators')
def list_actuators():
    return render_template("actuators.html", actuators=actuators)

@actuators_bp.route('/del_actuator')
def del_actuator():
    return render_template("remove_actuator.html", actuators=actuators)

@actuators_bp.route('/remove_actuator', methods=['GET', 'POST'])
def remove_actuator():
    global actuators
    if request.method == 'POST':
        actuator = request.form['name']
    else:
        actuator = request.args.get('name', None)

    if actuator in actuators:
        actuators.pop(actuator)
    return render_template("actuators.html", actuators=actuators)