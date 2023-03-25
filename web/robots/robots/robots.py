from flask import Flask, Response, render_template, request, make_response
import os

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("Welcome.html")


@app.route("/robots.txt")
def noindex():
    r = Response(
        response="User-Agent: *\nDisallow: /a37ls\n", status=200, mimetype="text/plain"
    )
    r.headers["Content-Type"] = "text/plain; charset=utf-8"
    return r


@app.route("/a37ls")
def a37ls():
    admin = request.cookies.get("admin")
    if admin == "1":
        return render_template(
            "Where are the robots.html", flag=os.environ.get("FLAG")
        )
    else:
        resp = make_response(render_template("NotAdmin.html"))
        resp.set_cookie("admin", "0")
        return resp
