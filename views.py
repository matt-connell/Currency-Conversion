from flask import Blueprint, render_template, request, redirect, url_for

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html")

@views.route("/CADtoUSD")
def cad_to_usd():
    return render_template("CADtoUSD.html", name="CAD to USD")

@views.route("/resultCADtoUSD",methods=['POST', "GET"])
def resultCADtoUSD():
    output = request.form.to_dict()
    temp = float(output["value"])
    result = 0.79 * temp
    return render_template("CADtoUSD.html", name=result)


#@views.route("/USDtoCAD")
#def cad_to_usd():
    #return render_template("USDtoCAD.html")

#@views.route("/resultUSDtoCAD",methods=['POST',"GET"])
#def resultUSDtoCAD():
    #output = request.form.to_dict()
    #temp = float(output["value"])
    #result = 1.26 * temp
    #return render_template("USDtoCAD.html", name=result)    