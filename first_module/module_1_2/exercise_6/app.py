from flask import Flask, render_template

app = Flask(__name__)

# Listen für Sensoren und Aktuatoren
sensoren_liste = ['Licht', 'Luftfeuchtigkeit', 'Beleuchtung']
aktuatoren_liste = ['Lampe', 'Schalter']

@app.route('/')
def startseite():
    raeume = {"Schlafzimmer": "/schlafzimmer", "Badezimmer": "/badezimmer"}
    return render_template('index.html', raeume=raeume)

# SCHLAFZIMMER
@app.route('/schlafzimmer')
def schlafzimmer():
    return render_template('schlafzimmer/schlafzimmer.html')

@app.route('/schlafzimmer/sensoren')
def schlafzimmer_sensoren():
    return render_template(
        'schlafzimmer/sensoren/schlafzimmer_sensoren.html', sensoren=sensoren_liste
    )

@app.route('/schlafzimmer/aktuatoren')
def schlafzimmer_aktuatoren():
    return render_template(
        'schlafzimmer/aktuatoren/schlafzimmer_aktuatoren.html', aktuatoren=aktuatoren_liste
    )

# BADEZIMMER
@app.route('/badezimmer')
def badezimmer():
    return render_template('badezimmer/badezimmer.html')

@app.route('/badezimmer/sensoren')
def badezimmer_sensoren():
    return render_template(
        'badezimmer/sensoren/badezimmer_sensoren.html', sensoren=sensoren_liste
    )

@app.route('/badezimmer/aktuatoren')
def badezimmer_aktuatoren():
    return render_template(
        'badezimmer/aktuatoren/badezimmer_aktuatoren.html', aktuatoren=aktuatoren_liste
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
