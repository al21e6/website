from flask import Blueprint, jsonify, render_template, request

legal_bp = Blueprint("legal_bp", __name__)


@legal_bp.route("/", methods=["GET"])
def get():
    print(__name__, "get")
    return render_template("legal.html"), 200
