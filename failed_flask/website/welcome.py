from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from website.auth import login_required
from website.db import get_db

bp = Blueprint("welcome", __name__)


@bp.route("/blog")
def index():
    return render_template("welcome/essay.html")
