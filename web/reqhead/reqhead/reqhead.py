from flask import Flask, Response, request
import os

app = Flask(__name__)

@app.route("/")
def noindex():
    print(request.base_url)
    if request.headers.get("user-agent") == "GammaBrowser":
        if request.headers.get("referer") == "request.base_url":
            if request.headers.get("DNT") == "1":
                r = Response(
                    response=os.environ.get("FLAG"), status=200, mimetype="text/plain"
                )
            else:
                r = Response(
                    response="User who are being tracked not allowed.",
                    status=200,
                    mimetype="text/plain",
                )
        else:
            r = Response(
                response="Users visiting from another site are not trusted.",
                status=200,
                mimetype="text/plain",
            )
    else:
        r = Response(
            response="Sorry, Only users using a special browser named GammaBrowser are allowed.",
            status=200,
            mimetype="text/plain",
        )
    r.headers["Content-Type"] = "text/plain; charset=utf-8"
    return r
