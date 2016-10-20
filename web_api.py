from flask import Flask, render_template, request, redirect, url_for

"""
Running web server with flask.

- when you want to connect to outside server with web api.
- when you want to check the graph on the browser.

exec below if you want to use development mode.
$ export FLASK_DEBUG=1

"""

app = Flask(__name__)


@app.route('/')
def index():
    return "web_api test"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
