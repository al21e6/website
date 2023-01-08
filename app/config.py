import ast
import json
import os
import secrets
from dotenv import load_dotenv

load_dotenv()


class Config:

    GITHUB_SECRET = os.getenv("GITHUB_SECRET")

    JSON_SORT_KEYS = False  # do not alphabetically sort when converting to JSON

    MAIL_SERVER = os.getenv("MAIL_SERVER", "")
    MAIL_PORT = os.getenv("MAIL_PORT", "")
    MAIL_USERNAME = os.getenv("MAIL_USERNAME", "")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "")
    MAIL_USE_TLS = ast.literal_eval(os.getenv("MAIL_USE_TLS", "False"))
    MAIL_USE_SSL = ast.literal_eval(os.getenv("MAIL_USE_SSL", "False"))

    LNBITS_HOST = os.getenv("LNBITS_HOST")
    LNBITS_READ_KEY = os.getenv("LNBITS_READ_KEY")
    LNBITS_WEBHOOK = os.getenv("LNBITS_WEBHOOK")

    SECRET_KEY = secrets.token_urlsafe(32)  # secret key from server to client

    WEBSITE_ABOUT = os.getenv("WEBSITE_ABOUT", "")  # website specific fields
    WEBSITE_NAME = os.getenv("WEBSITE_NAME", "")
    WEBSITE_LOGO = os.getenv("WEBSITE_LOGO", "")
    WEBSITE_SLOGAN = os.getenv("WEBSITE_SLOGAN", "")
    WEBSITE_URL = os.getenv("WEBSITE_URL", "")
    WEBSITE_GITHUB = os.getenv("WEBSITE_GITHUB", "")
    WEBSITE_INSTAGRAM = os.getenv("WEBSITE_INSTAGRAM", "")
    WEBSITE_TIKTOK = os.getenv("WEBSITE_TIKTOK", "")
    WEBSITE_TWITTER = os.getenv("WEBSITE_TWITTER", "")
