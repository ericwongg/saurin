from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def main():
    post_button = request.args.get("post_button",None)
    
    if post_button == login:
        render_template("login.html")
    elif post_button == register:
        render_template("register.html")
    else:
        render_template("main.html")
