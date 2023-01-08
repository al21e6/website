from flask import Blueprint, jsonify, render_template, request

about_bp = Blueprint("about_bp", __name__)


@about_bp.route("/", methods=["GET"])
def get():
    print(__name__, "get")
    return render_template("about.html"), 200
