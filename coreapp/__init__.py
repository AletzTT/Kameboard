from flask_migrate import Migrate
from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'b51a23e0ca28e5b61766e2e0c1fc47c6c10e43ac'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://kameadmin@localhost:s4rTf4SZoy@localhost/kameboard'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = "Porfavor Inicia Sesión"

    db.init_app(app)
    migrate.init_app(app, db)
    
    #Blueprints
    from .auth import auth_bp
    app.register_blueprint(auth_bp)
    
    from .admin import admin_bp
    app.register_blueprint(admin_bp)
    
    from .public import public_bp
    app.register_blueprint(public_bp)
    
    # Custom error handlers
    register_error_handlers(app)
    
    return app

def register_error_handlers(app):

    @app.errorhandler(500)
    def base_error_handler(e):
        return render_template('500.html'), 500

    @app.errorhandler(404)
    def error_404_handler(e):
        return render_template('404.html'), 404
    
    @app.errorhandler(401)
    def error_404_handler(e):
        return render_template('401.html'), 401