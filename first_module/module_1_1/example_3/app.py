# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def startseite():
    return "Inhalts der Startseite!"

@app.route('/sensoren')
def sensoren():
    return "Sensoren auflisten"

@app.route('/aktuatoren')
def aktuatoren():
    return "Aktuatoren auflisten"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
