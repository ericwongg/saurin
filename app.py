from flask import Flask, render_template, request, redirect
import pymongo

app = Flask(__name__)

login = False

@app.route("/", method=["GET", "POST"])
def main():
    button = request.args.get("b",None)
    if button == 'login':
        login()
    elif button == 'regist':
        register()
    else:
        return render_template("main.html")

@app.route("/login", method=["GET","POST"])
def login():
    user_id = request.args.get("uname",None)
    password = request.args.get("pass",None)
    if request.method == 'POST':
        login = True
        #check if matches database
        user()
    else:
        flash("Invalid Username or Password!")
        return render_template("login.html")

@app.route("/logout", method=["GET","POST"])
def logout():
    button = request.args.get("b",None)
    login = False
    if button == 'home':
        main()
    else:
        return render_template("logout.html")
    
@app.route("/register", method=["GET","POST"])
def register():
    user_id = request.args.get("uname",None)
    password = request.args.get("pass",None)
    if request.method == "POST":
        #put new data into database
        flash("Successfully registered!")
        return render_template("login.html")
    else:
        return redirect("/register")

@app.route("/user1", method=["GET","POST"]))
#private pages
def user1():
    if (login == False):
        button = request.args.get("b",None)
        if button == 'next':
            user2()
        else:
            return render_template("user1.html")
    else:
        return redirect("/main")
    
@app.route("/user2", method=["GET","POST"]))
#private pages
def user2():
    if (login == False):
        button = request.args.get("b",None)
        if button == 'next':
            user1()
        else:
            return render_template("user2.html")
    else:
        return redirect("/main")

@app.route("/public", method=["GET","POST"])
#public pages
def public():
    button = request.args.get("b", None)
    if button == 'home':
        main()
    else:
        return render_template("public.html")

#main
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=1234)
