from flask import Blueprint, render_template


demos_bp = Blueprint("demos_bp", __name__, template_folder="templates")


@demos_bp.route("/")
def home():
    return render_template("demos/index.html")
