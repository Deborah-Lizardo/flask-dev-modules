from flask import Flask, render_template

app = Flask(__name__)

# Startseite
@app.route('/')
def startseite():
    raeume = {"Schlafzimmer": "/schlafzimmer", "Badezimmer": "/badezimmer"}
    return render_template("index.html", raeume=raeume)

# Aktuatoren
@app.route('/aktuatoren')
def aktuatoren():
    aktuatoren_dict = {'Lampe': 1, 'Servomotor': 122}
    return render_template("aktuatoren.html", aktuatoren=aktuatoren_dict)

# Sensoren
@app.route('/sensoren')
def sensoren():
    sensoren_dict = {'T1': 56, 'T2': 25, 'T3': 15}
    return render_template("sensoren.html", sensoren=sensoren_dict)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8800, debug=True)
