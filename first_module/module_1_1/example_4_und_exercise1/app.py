# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def startseite():
    return """
<html>
<head>
<title>Mein Zuhause</title>
</head>
<body>
<h2>Mein Zuhause</h2>
<h3>Menü aufrufen:</h3>
<ul>
<li><a href="/sensoren">Sensoren auflisten</a></li>
<li><a href="/aktuatoren">Aktuatoren auflisten</a></li>
</ul>
</body>
</html>
"""

@app.route('/sensoren')
def sensoren():
    return """
<html>
<head>
<title>Mein Zuhause</title>
</head>
<body>
<h1>Sensoren</h1>
<ul>
<li>Feuchtigkeitssensor</li>
<li>Temperatursensor</li>
<li>Helligkeitssensor</li>
</ul>
<p>Zurück zur <a href="/">Startseite</a>!</p>
</body>
</html>
"""

@app.route('/aktuatoren')
def aktuatoren():
    return """
<html>
<head>
<title>Mein Zuhause</title>
</head>
<body>
<h1>Aktuatoren</h1>
<ul>
<li>Relais</li>
<li>Motor</li>
<li>LED</li>
</ul>
<p>Zurück zur <a href="/">Startseite</a>!</p>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
