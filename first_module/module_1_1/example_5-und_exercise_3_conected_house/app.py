from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def startseite():
    return render_template("index.html")

@app.route('/aktuatoren')
def aktuatoren():
    aktuatoren = ['Lampe', 'Servomotor']
    return render_template("aktuatoren.html", aktuatoren=aktuatoren)

@app.route('/sensoren')
def sensoren():
    sensoren = ['Temperatur', 'Luftfeuchtigkeit', 'Helligkeit']
    return render_template("sensoren.html", sensoren=sensoren)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
