from flask import Flask, render_template, request, session, logging, url_for,redirect,json,flash
app = Flask(__name__)

@app.route("/")
def inicio():   
    return redirect(url_for("alec"))

@app.route("/alec", methods=["GET","POST"])
def alec():
    if request.method=="POST":
        return redirect(url_for("love"))
    return render_template("alec.html")

@app.route("/love", methods=["GET","POST"])
def love():

    return render_template("love.html")


if __name__=="__main__":
    app.run(debug=True)