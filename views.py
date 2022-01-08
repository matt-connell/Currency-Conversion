from flask import Blueprint, render_template, request, redirect, url_for

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html", name="Matthew")

@views.route("/CADtoUSD")
def cad_to_usd():
    return render_template("CADtoUSD.html", name="CAD to USD")
