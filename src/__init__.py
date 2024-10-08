import os
from flask import Flask, render_template

from .views import avistamento, avistamento

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'mabuya.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .data import db
    db.init_app(app)

    from .views import sobre, avistamento, especies
    app.register_blueprint(avistamento.bp)
    app.register_blueprint(sobre.bp)
    app.register_blueprint(especies.bp)

    @app.route('/')
    def home():
        return render_template('home.html')

    return app