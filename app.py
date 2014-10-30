from flask import Flask, render_template, request, redirect

app = Flask(__name__)

login = False

@app.route("/")
def main():
    render_template("main.html")

@app.route("/login", method=["GET","POST"])

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
