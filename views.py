from flask import Blueprint, render_template, request, redirect, url_for

#this statement allows all routes to be stored in a sepreate python file
views = Blueprint(__name__, "views")


#assigning routes that link to the same home page
@views.route("/")
@views.route("home")
@views.route("/index")
def home():
    return render_template("index.html")


#the route for Cad -> Usd conversion
@views.route("/CADtoUSD")
def cad_to_usd():
    #assign name variable to current conversion and render html file
    return render_template("CADtoUSD.html", name="CAD to USD")

#this route is for when conversion button is clicked in html file
@views.route("/resultCADtoUSD",methods=['POST', "GET"])
def resultCADtoUSD():
    output = request.form.to_dict()
    #typecast output to a float variable
    temp = float(output["value"])
    #format to 2 decimal places
    format_currency = "{:.2f}".format(temp)
    #conversion calculation
    result = 0.79 * temp
    #format to 2 decimal places
    format_float = "{:.2f}".format(result)
    #assign variables the constant and result of calculation
    return render_template("CADtoUSD.html", result=format_float, currency=format_currency)

#the route for USD to CAD conversion
@views.route("/USDtoCAD")
def usd_to_cad():
    #assign name variable to current conversion and render html file
    return render_template("USDtoCAD.html")

#this route is for when conversion button is clicked in html file
@views.route("/resultUSDtoCAD",methods=['POST',"GET"])
def resultUSDtoCAD():
    output = request.form.to_dict()
    #type cast to float variable
    temp = float(output["value"])
    #format number to 2 decimal places
    format_currency = "{:.2f}".format(temp)
    #conversion calculation
    result = 1.26 * temp
    #format number to 2 decimal places
    format_float = "{:.2f}".format(result)
    #assign variables and render html file
    return render_template("USDtoCAD.html", result=format_float, currency=format_currency)    

#the route for CAD to EURO conversion
@views.route("/CADtoEURO")
def cad_to_euro():
    #assign name variable to current conversion and render html file
    return render_template("CADtoEURO.html")

#this route is for when conversion button is clicked in html file
@views.route("/resultCADtoEURO",methods=['POST',"GET"])
def resultCADtoEURO():
    output = request.form.to_dict()
    #type cast to float variable
    temp = float(output["value"])
    #format number to 2 decimal places
    format_currency = "{:.2f}".format(temp)
    #conversion calculation
    result = 0.698117 * temp
    #format number to 2 decimal places
    format_float = "{:.2f}".format(result)
    #assign variables and render html file
    return render_template("CADtoEURO.html", result=format_float, currency=format_currency)    

#the route for EURO to CAD conversion
@views.route("/EUROtoCAD")
def euro_to_cad():
    #assign name variable to current conversion and render html file
    return render_template("EUROtoCAD.html")

#this route is for when conversion button is clicked in html file
@views.route("/resultEUROtoCAD",methods=['POST',"GET"])
def resultEUROtoCAD():
    output = request.form.to_dict()
    #type cast to float variable
    temp = float(output["value"])
    #format number to 2 decimal places
    format_currency = "{:.2f}".format(temp)
    #conversion calculation
    result = 1.43243 * temp
    #format number to 2 decimal places
    format_float = "{:.2f}".format(result)
    #assign variables and render html file
    return render_template("EUROtoCAD.html", result=format_float, currency=format_currency)   