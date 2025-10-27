from flask import Flask, render_template

app = Flask(__name__)

# Página inicial
@app.route('/')
def startseite():
    raeume = {"Schlafzimmer": "/schlafzimmer", "Badezimmer": "/badezimmer"}
    return render_template("index.html", raeume=raeume)

# SCHLAFZIMMER
@app.route('/schlafzimmer')
def schlafzimmer():
    sensoren_dict = {'Feuchtigkeit': 22, 'Temperatur': 23, 'Beleuchtung': 1034}
    aktuatoren_dict = {'Lampe': 1, 'Schalter': 0}
    return render_template("schlafzimmer.html", sensoren=sensoren_dict, aktuatoren=aktuatoren_dict)

# BADEZIMMER
@app.route('/badezimmer')
def badezimmer():
    sensoren_dict = {'Feuchtigkeit': 24, 'Temperatur': 25, 'Beleuchtung': 1200}
    aktuatoren_dict = {'Lampe': 0, 'Schalter': 1}
    return render_template("badezimmer.html", sensoren=sensoren_dict, aktuatoren=aktuatoren_dict)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
