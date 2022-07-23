import pickle
from flask import Blueprint, render_template


demos_bp = Blueprint("demos_bp", __name__, template_folder="templates")


@demos_bp.route("/")
def home():
    return render_template("demos/index.html")


@demos_bp.route("/neural_network_mnist")
def neural_network_mnist():
    return render_template("demos/neural_network_mnist.html")
