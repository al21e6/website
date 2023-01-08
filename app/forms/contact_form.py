from flask_wtf import FlaskForm, RecaptchaField
from wtforms import SelectField, SubmitField, StringField, TextAreaField
import wtforms.validators as validators


class ContactForm(FlaskForm):

    email = StringField(
        "Your email",
        validators=[validators.DataRequired()],
        render_kw={"placeholder": "email@example.com", "class": "u-full-width"},
    )

    subject = SelectField(
        "Select a subject",
        choices=[
            ("hello", "Hello"),
        ],
        render_kw={"class": "u-full-width"},
    )

    message = TextAreaField(
        "Message",
        [validators.DataRequired(), validators.length(max=200)],
        render_kw={"placeholder": "Hello …", "class": "u-full-width"},
    )

    # recaptcha = RecaptchaField()

    submit = SubmitField(
        "Send",
        render_kw={
            "class": "button-primary-hollow",
            "style": "color: white; text-transform: none; font-size: initial;",
        },
    )
