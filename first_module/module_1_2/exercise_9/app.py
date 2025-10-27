
from flask import Flask, render_template

app = Flask(__name__)

sensoren = {'Temperatur': 23, 'Luftfeuchtigkeit': 22, 'Beleuchtung': 10}
aktuatoren = {'Lampe': 1, 'Schalter': 0}

@app.route('/')
def startseite():
    return render_template("index.html")

@app.route('/sensoren')
def sensors():
    return render_template("sensoren.html", sensoren=sensoren)

@app.route('/aktuatoren')
def actuators():
    return render_template("aktuatoren.html", aktuatoren=aktuatoren)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
