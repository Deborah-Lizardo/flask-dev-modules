from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/upload_file', methods=['POST'])
def success():
    f = request.files['file']
    upload_folder = 'static/img/'

    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    f.save(os.path.join(upload_folder, f.filename))
    return "Arquivo enviado com sucesso!"

# Handlers de erros
@app.errorhandler(401)
def error_401(error):
    return render_template('401.html'), 401

@app.errorhandler(403)
def error_403(error):
    return render_template('403.html'), 403

@app.errorhandler(404)
def error_404(error):
    return render_template('404.html'), 404

@app.errorhandler(405)
def error_405(error):
    return render_template('405.html'), 405

@app.errorhandler(500)
def error_500(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
