import os
import sys
from dotenv import load_dotenv
from flask import Flask, redirect, url_for
from flask_mail import Mail

# sys.path.append("../flask_lnbits/flask_lnbits")
from flask_lnbits import LNbits

from flask_qrcode import QRcode
from flask_wtf.csrf import CSRFProtect
from app.config import Config

csrf = CSRFProtect()
lnbits = LNbits()
mail = Mail()
qr_code = QRcode()


def create_app() -> Flask:

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(Config)

    csrf.init_app(app=app)
    lnbits.init_app(app=app)
    mail.init_app(app=app)
    qr_code.init_app(app=app)

    with app.app_context():

        from app.blueprints.about_bp import about_bp
        from app.blueprints.contact_bp import contact_bp
        from app.blueprints.index_bp import index_bp
        from app.blueprints.legal_bp import legal_bp
        from app.blueprints.pay_bp import pay_bp
        from app.blueprints.webhooks_bp import webhooks_bp

        app.register_blueprint(about_bp, url_prefix="/about")
        app.register_blueprint(contact_bp, url_prefix="/contact")
        app.register_blueprint(index_bp, url_prefix="/")
        app.register_blueprint(legal_bp, url_prefix="/legal")
        app.register_blueprint(pay_bp, url_prefix="/pay")
        app.register_blueprint(webhooks_bp, url_prefix="/webhooks")

        return app
