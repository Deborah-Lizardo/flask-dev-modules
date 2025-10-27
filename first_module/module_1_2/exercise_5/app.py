from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sensoren')
def sensor():
    sensoren = ['Temperatur', 'Luftfeuchtigkeit', 'Beleuchtung']
    return render_template("sensoren.html", sensoren=sensoren)

@app.route('/aktuatoren')
def aktuatoren():
    aktuatoren = ['Lampe', 'Servomotor']
    return render_template("aktuatoren.html", aktuatoren=aktuatoren)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
