from flask import Flask, render_template, request, redirect, flash, session
import pymongo, data

app = Flask(__name__)
#app.session_interface = MongoSessionInterface(db='saurin')

login = False

@app.route("/", methods=["GET", "POST"])
def main():
    button = request.args.get("b",None)
    if button == 'login':
        login()
    elif button == 'regist':
        register()
    else:
        return render_template("main.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        user_id = request.args.get("uname",None)
        password = request.args.get("pass",None)
        login = True
        #check login, send to private page if successful
        if data.check(user_id, password):
            private1()
        else:
            flash("Invalid Username or Password!")
            return redirect("/login")
    
@app.route("/logout", methods=["GET","POST"])
def logout():
    button = request.args.get("b",None)
    login = False
    if button == 'home':
        flash("Successfully logged out")
        return main()
    else:
        return render_template("logout.html")
    
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        user_id = request.args.get("uname",None)
        password = request.args.get("pass",None)
        #add new data to db, if taken dont do anything
        if data.addNew(user_id, password):
            flash("Successfully registered!")
            return render_template("login.html")
        else:
            flash("Sorry, the username is already taken.")
            return redirect("/register")


@app.route("/private1", methods=["GET","POST"])
#private pages
def private1():
    if (login == False):
        button = request.args.get("b",None)
        if button == 'next':
            private2()
        else:
            return render_template("private1.html")
    else:
        return redirect("/main")
    
@app.route("/private2", methods=["GET","POST"])
#private pages
def private2():
    if (login == False):
        button = request.args.get("b",None)
        if button == 'next':
            private1()
        else:
            return render_template("private2.html")
    else:
        return redirect("/main")

@app.route("/public", methods=["GET","POST"])
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
