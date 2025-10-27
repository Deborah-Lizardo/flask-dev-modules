from flask import Flask

app = Flask(__name__)

@app.route('/')
def startseite():
    return """
<html>
<head><title>Vernetztes Haus</title></head>
<body>
<h1>Willkommen im vernetzten Haus!</h1>
<h3>Wählen Sie ein Zimmer:</h3>
<ul>
<li><a href="/room/bedroom">Schlafzimmer</a></li>
<li><a href="/room/bathroom">Badezimmer</a></li>
</ul>
</body>
</html>
"""

@app.route('/room/bedroom')
def schlafzimmer():
    return """
<html>
<head><title>Schlafzimmer</title></head>
<body>
<h1>Schlafzimmer</h1>
<h3>Was möchten Sie sehen?</h3>
<ul>
<li><a href="/room/bedroom/sensors">Sensoren im Schlafzimmer</a></li>
<li><a href="/room/bedroom/actuators">Aktuatoren im Schlafzimmer</a></li>
</ul>
<p><a href="/">Zurück zur Startseite</a></p>
</body>
</html>
"""

@app.route('/room/bedroom/sensors')
def schlafzimmer_sensoren():
    return """
<html>
<head><title>Sensoren im Schlafzimmer</title></head>
<body>
<h1>Sensoren im Schlafzimmer</h1>
<ul>
<li>Helligkeitssensor: 200 Lux</li>
</ul>
<p><a href="/room/bedroom">Zurück zum Schlafzimmer</a></p>
</body>
</html>
"""

@app.route('/room/bedroom/actuators')
def schlafzimmer_aktuatoren():
    return """
<html>
<head><title>Aktuatoren im Schlafzimmer</title></head>
<body>
<h1>Aktuatoren im Schlafzimmer</h1>
<ul>
<li>Lichtschalter: Ausgeschaltet</li>
</ul>
<p><a href="/room/bedroom">Zurück zum Schlafzimmer</a></p>
</body>
</html>
"""

@app.route('/room/bathroom')
def badezimmer():
    return """
<html>
<head><title>Badezimmer</title></head>
<body>
<h1>Badezimmer</h1>
<h3>Was möchten Sie sehen?</h3>
<ul>
<li><a href="/room/bathroom/sensors">Sensoren im Badezimmer</a></li>
<li><a href="/room/bathroom/actuators">Aktuatoren im Badezimmer</a></li>
</ul>
<p><a href="/">Zurück zur Startseite</a></p>
</body>
</html>
"""

@app.route('/room/bathroom/sensors')
def badezimmer_sensoren():
    return """
<html>
<head><title>Sensoren im Badezimmer</title></head>
<body>
<h1>Sensoren im Badezimmer</h1>
<ul>
<li>Feuchtigkeitssensor: 60%</li>
</ul>
<p><a href="/room/bathroom">Zurück zum Badezimmer</a></p>
</body>
</html>
"""

@app.route('/room/bathroom/actuators')
def badezimmer_aktuatoren():
    return """
<html>
<head><title>Aktuatoren im Badezimmer</title></head>
<body>
<h1>Aktuatoren im Badezimmer</h1>
<ul>
<li>Intelligente Lampe: Eingeschaltet</li>
</ul>
<p><a href="/room/bathroom">Zurück zum Badezimmer</a></p>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
