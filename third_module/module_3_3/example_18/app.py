from fileinput import filename
from flask import *

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.errorhandler(404)
def not_found_404(error):
    return render_template('404.html'), 404

@app.errorhandler(405)
def not_allowed_405(error):
    return "Não autorizado", 405

@app.errorhandler(401)
def not_authorized_401(error):
    return "Usuário não autorizado", 401


@app.route('/upload_file', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save('static/img/' + f.filename)
        return "ok"
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
