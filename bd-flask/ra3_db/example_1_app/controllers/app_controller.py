#app_controller.py
from flask import Flask, render_template, request

def create_app():
    app = Flask(__name__,
                template_folder="./views/",
                static_folder="./static/",
                root_path="/")
    
    @app.route('/')
    def index():
        return render_template("home.html")
    
    return app
