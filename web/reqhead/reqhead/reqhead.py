from flask import Flask, Response, request
import os

app = Flask(__name__)

@app.route("/")
def noindex():
    print(request.base_url)
    if request.headers.get("user-agent") != "PuPuBrowser":
        return Response(
            response="Sorry, Only users using a special browser named PuPuBrowser are allowed.",
            status=200,
            mimetype="text/plain",
        )
    
    if request.headers.get("referer") != request.base_url:
        return Response(
            response="Users visiting from another site are not trusted.",
            status=200,
            mimetype="text/plain",
        )
    
    if request.headers.get("DNT") == "1":
        return Response(
            response="User who are being tracked not allowed.",
            status=200,
            mimetype="text/plain",
        )
    
    return Response(
        response=os.environ.get("FLAG"), status=200, mimetype="text/plain"
    )
