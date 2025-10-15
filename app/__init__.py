import os
from flask import Flask, session
from datetime import timedelta

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = os.environ.get('SESSION_SECRET', 'dev-secret-key-change-in-production')
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'static', 'uploads')
    app.config['DATABASE'] = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ecommerce.db')
    
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], 'products'), exist_ok=True)
    os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], 'profiles'), exist_ok=True)
    
    from app.blueprints.auth import auth_bp
    from app.blueprints.shop import shop_bp
    from app.blueprints.admin import admin_bp
    from app.blueprints.cart import cart_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(shop_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(cart_bp)
    
    @app.context_processor
    def inject_cart_count():
        cart = session.get('cart', {})
        cart_count = sum(item['quantity'] for item in cart.values())
        return {'cart_count': cart_count}
    
    return app
