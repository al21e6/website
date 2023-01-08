# See: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure

from threading import Thread
from typing import Dict, Optional
from flask import current_app
from flask_mail import Message
import html2text  # https://en.wikipedia.org/wiki/Aaron_Swartz
from app import mail


def _send_async(app, message: Message):
    """Send a message asynchronously.

    Args:
        app: The application instance stored inside the proxy object, current_app.
        message: The message to send.
    """
    print(__name__, "_send_async")
    with app.app_context():
        print(mail, message)
        mail.send(message)


def send(
    sender: str,
    recipient: str,
    subject: str,
    html: str,
    attachment: Optional[Dict[str, str]] = None,
):
    """Sends an email to a recipient from the default mail sender asynchronously.

    Args:
        sender: The sender of the email.
        recipient: The recipient of the email.
        subject: The subject of the email.
        html_body: The HTML mark up of the email.
        attachment: An optional dictionary representing an attachment with the
            following keys:
                "filename": the filename of the attachment.
                "content_type": file MIME type, application/pdf.
                "data": the raw file data.
                "disposition": the content disposition.
            e.g.
                attachment = {"filename": "foo.bar"}

    """
    print(__name__, "send")
    bcc = [current_app.config.get("MAIL_USERNAME")]
    body = html2text.html2text(html)  # convert to plain text
    message = Message(
        subject, sender=sender, bcc=bcc, recipients=[recipient], html=html, body=body
    )
    if attachment:
        message.attach(**attachment)
    args = (current_app._get_current_object(), message)
    thread = Thread(target=_send_async, args=args)
    thread.start()
