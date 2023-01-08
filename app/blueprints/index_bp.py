from flask import Blueprint, jsonify, redirect, render_template, request, url_for

index_bp = Blueprint("index_bp", __name__)


@index_bp.route("/", methods=["GET"])
def get():
    print(__name__, "get")
    return render_template("index.html"), 200
