from flask import Flask , render_template,request

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "Not" and password=="Noot":
        return render_template("welcome.html" ,name = username)
    else:
        return "Invalid Credentials"

