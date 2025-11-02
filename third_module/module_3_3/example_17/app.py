from fileinput import filename
from flask import *

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/upload_file', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save('static/img/' + f.filename)
        return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
