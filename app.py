from flask import Flask
from views.clustering_view import clustering_view

def create_app():
    app = Flask(__name__)
    app.register_blueprint(clustering_view)
    return app
