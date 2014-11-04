from flask import Flask, render_template, request, redirect, flash, session
import data

app = Flask(__name__)
app.session_interface = MongoSessionInterface(db='saurin')

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
        #check login, send to private page if successful
        if data.check(user_id, password):
            private1()
        else:
            flash("Invalid Username or Password!")
            return render_template("login.html")

@app.route("/logout", method=["GET","POST"])
def logout():
    button = request.args.get("b",None)
    login = False
    if button == 'home':
        flash("Successfully logged out")
        main()
    else:
        return render_template("logout.html")
    
@app.route("/register", method=["GET","POST"])
def register():
    user_id = request.args.get("uname",None)
    password = request.args.get("pass",None)
    if request.method == "POST":
        #need to check if username in database already
        #true if user not in, false otherwise
        #if separate.checkuser(user_id):
        #flash("Successfully registered!")
        #return render_template("login.html")
        #else:
        #flash("Sorry, the username is already taken")
        #return redirect("/register")
        #put new data into database
        if data.addNew(user_id, password):
            flash("Successfully registered!")
            return render_template("login.html")
        else:
            flash("Sorry, the username is already taken.")
            return redirect("/register")
    else:
        return redirect("/register")

@app.route("/user1", method=["GET","POST"]))
#private pages
def private1():
    if (login == False):
        button = request.args.get("b",None)
        if button == 'next':
            user2()
        else:
            return render_template("private1.html")
    else:
        return redirect("/main")
    
@app.route("/user2", method=["GET","POST"]))
#private pages
def private2():
    if (login == False):
        button = request.args.get("b",None)
        if button == 'next':
            user1()
        else:
            return render_template("private2.html")
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
