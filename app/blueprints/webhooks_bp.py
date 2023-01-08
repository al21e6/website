import hashlib
import hmac
import six
import subprocess
from flask import Blueprint, jsonify, request
from flask import current_app as app

webhooks_bp = Blueprint("webhooks_bp", __name__)


@webhooks_bp.route("/github", methods=["GET", "POST"])
def github():
    """Triggered when a push request is made to GitHub. To add a GitHub webhook go to the
    following URL:

        https://github.com/<USER>/<REPO>/settings/hooks/new

    and add these parameters:

        Payload URL: https://<SERVER_IP>:<SERVER_PORT>/api/webhooks/github
        content type: application/json
        secret: <GITHUB_SECRET>

    """
    print(__name__, "github")
    try:
        secret = app.config["GITHUB_SECRET"].encode("utf-8")
        digest = six.text_type(hmac.new(secret, request.data, hashlib.sha1).hexdigest())
        sig_parts = request.headers["X-Hub-Signature"].split("sha1=")
        if not hmac.compare_digest(sig_parts[1], digest):
            raise ValueError("GITHUB_SECRET does not match.")
        result = subprocess.run(
            ["git", "pull"], stdout=subprocess.STDOUT, stderr=subprocess.STDOUT
        )
        if result.returncode != 0:
            raise Exception((str(result.stdout)))
    except Exception as e:
        return jsonify({"Error": f"{e}"}), 400
    else:
        return jsonify({}), 200
