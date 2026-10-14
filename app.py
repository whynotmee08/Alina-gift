from idlelib import statusbar
from mimetypes import init
from operator import add

from flask import Flask, render_template
from pip._internal.vcs import git

app = Flask(__name__)
@app.route('/')
def index():
    photos =[""]
    return render_template("index.html", photos=photos)
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
