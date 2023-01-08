from decimal import Decimal
import json
from flask import Blueprint, flash, jsonify, render_template, request
from app.forms.pay_form import PayForm


from app import lnbits

pay_bp = Blueprint("pay_bp", __name__)


@pay_bp.route("", methods=["GET"])
@pay_bp.route("/", methods=["GET"])
def get():
    print(__name__, "get")
    data = lnbits.get_lnurlp()
    form = PayForm()
    return render_template("pay.html", data=data, form=form), 200


@pay_bp.route("/invoice", methods=["POST"])
def invoice():
    print(__name__, "invoice")
    form = PayForm()
    if form.validate_on_submit():
        data = lnbits.create_invoice(
            unit=form.unit.data,
            amount=form.amount.data,
            memo=form.memo.data,
        )
        flash(message="Please pay the invoice!", category="success")
        return render_template("pay-invoice.html", data=data), 200
    flash(
        message="Error generating invoice. Please refresh and try again",
        category="error",
    )
    return redirect(url_for("pay_bp.get"))
