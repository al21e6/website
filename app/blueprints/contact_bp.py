from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from app import mail
from app.forms.contact_form import ContactForm
from app.utils.email import send

contact_bp = Blueprint("contact_bp", __name__)


@contact_bp.route("/", methods=["GET"])
def get():
    print(__name__, "get")
    form = ContactForm()
    return render_template("contact.html", form=form)


@contact_bp.route("/send-message", methods=["POST"])
def send_message():
    print(__name__, "send_message")
    form = ContactForm()
    if form.validate_on_submit():
        send(
            sender=form.email.data,
            recipient=mail.username,
            subject=form.subject.data,
            html=form.message.data,
        )
        flash(message="Email sent!", category="success")
        return redirect(url_for("contact_bp.get"))
    return render_template("contact.html", form=form)
