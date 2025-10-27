from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sensor')
def sensor():
    sensoren = {'T1':56, 'T2':25, 'T3':15}
    return render_template("sensoren.html", sensoren=sensoren)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
