from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def startseite():
    return render_template('index.html')

#SCHLAFZIMMER-BEEDROM

@app.route('/schlafzimmer')
def schlafzimmer():
    return render_template('schlafzimmer.html')

@app.route('/schlafzimmer/sensoren')
def schlafzimmer_sensoren():
    return render_template ('schlafzimmer/sensoren/schlafzimmer_sensoren.html')

@app.route('/schlafzimmer/aktuatoren')
def schlafzimmer_aktuatoren():
    return render_template ('schlafzimmer/aktuatoren/schlafzimmer_aktuatoren.html')

#BADEZIMMER - BATHROOM

@app.route('/badezimmer')
def badezimmer():
    return render_template("badezimmer.html")

@app.route('/badezimmer/sensoren')
def badezimmer_sensoren():
    return render_template("badezimmer/sensoren/badezimmer_sensoren.html")

@app.route('/badezimmer/aktuatoren')
def badezimmer_aktuatoren():
    return render_template("badezimmer/aktuatoren/badezimmer_aktuatoren.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
