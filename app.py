from flask import Flask, render_template, request, redirect
import mongo

app = Flask(__name__)

login = False

@app.route("/", method=["GET", "POST"])
def main():
    return render_template("main.html")
    button = request.args.get("b",None)
    if button == login:
        login()
    elif button == regist:
        register()
    else:
        return render_template("main.html")

@app.route("/login", method=["GET","POST"])
def login():
    error = None
    if request.method == 'POST':
        user_id = request.args.get("uname",None)
        password = request.args.get("pass",None)
        

@app.route("/user")
#private pages
def user():
    if (login == False):
        return
        

@app.route("/public")
#public pages


if __name__ == "__main__":
    app.debug = True
    app.run()
