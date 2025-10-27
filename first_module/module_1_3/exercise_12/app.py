from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

raeume = {"Schlafzimmer": "/schlafzimmer", "Badezimmer": "/badezimmer"}

@app.route('/room')
def room():
    raeume = {"Schlafzimmer": "/schlafzimmer", "Badezimmer": "/badezimmer"}
    return render_template("room.html", raeume=raeume)

@app.route('/schlafzimmer')
def schlafzimmer():
    sensoren = ['Temperatur', 'Licht']
    aktuatoren = ['Lampe', 'Servo']
    return render_template("schlafzimmer.html", sensoren=sensoren, aktuatoren=aktuatoren)

@app.route('/badezimmer')
def badezimmer():
    sensoren = ['Feuchtigkeit', 'Temperatur']
    aktuatoren = ['Licht', 'Lüfter']
    return render_template("badezimmer.html", sensoren=sensoren, aktuatoren=aktuatoren)

@app.route('/devices')
def devices():
    return render_template("devices.html")

@app.route('/sensoren')
def sensoren():
    return render_template("sensoren.html", sensoren=['Temperatur', 'Feuchtigkeit', 'Licht'])

@app.route('/aktuatoren')
def aktuatoren():
    return render_template("aktuatoren.html", aktuatoren=['Lampe', 'Servo', 'Lüfter'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
