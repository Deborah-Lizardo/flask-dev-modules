from flask import Flask, render_template, request
app= Flask( __name__ )

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/actuator')
def actuator():
    actuators = {'lamp': 1, 'serv motor': 122}
    return render_template("actuators.html", actuators=actuators)

@app.route('/sensor')
def sensor():
    sensors = {'temperature':23, 'humidity':22,'luminosity':10}
    return render_template("sensors.html", sensors=sensors)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
