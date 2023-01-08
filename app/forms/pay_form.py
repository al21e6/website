from flask_wtf import FlaskForm, RecaptchaField
from wtforms import DecimalField, SelectField, SubmitField, TextAreaField
import wtforms.validators as validators


class PayForm(FlaskForm):

    amount = DecimalField(places=2, validators=[validators.DataRequired()])

    unit = SelectField(
        "Select a unit",
        choices=[("sat", "sat"), ("USD", "$"), ("GBP", "£"), ("EUR", "€")],
        render_kw={"class": "u-full-width"},
    )

    memo = TextAreaField(
        "Memo",
        [validators.length(max=200)],
        render_kw={"placeholder": "Invoice for …", "class": "u-full-width"},
    )

    # recaptcha = RecaptchaField()

    submit = SubmitField(
        "Create",
        render_kw={
            "class": "button-primary-hollow",
            "style": "color: white; text-transform: none; font-size: initial;",
        },
    )
