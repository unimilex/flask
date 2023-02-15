from flask import Flask, render_template, request,make_response

dic={}
app = Flask(__name__)

@app.route("/")
@app.route("/color")
def index():
    
    background_color=request.cookies.get("background_color","#FFFF")
    response=render_template("mostrar.html",background_color=background_color)
    return response
@app.route("/color", methods=["POST"])
def cambiar_fondo():
    
        background_color = request.form["fondo"]
        resp = make_response(render_template("mostrar.html",background_color=background_color))
        resp.set_cookie('background_color',background_color)
        return resp 



    

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html",error="Lo sentimos. Página no encontrada..."), 404

    
if __name__ == '__main__':
    app.run(debug=True)