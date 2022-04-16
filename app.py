import os
import time
from datetime import datetime

from flask import Flask,make_response, request, render_template, abort, Response

app = Flask(__name__)

app_folder = os.path.dirname(os.path.abspath(__file__))


def generate_file(filename, content):
    with open(f"{app_folder}/myPersonalSite/content/post/{filename}", "w") as f:
        f.write(content)
    
    os.chdir(f"{app_folder}/myPersonalSite")
    os.system("hugo")


@app.route("/editor/")
def editor():
    return render_template("index.html")

@app.route("/editor-post/", methods=['POST'])
def editor_post():
    content = request.json.get('content')
    title = '"' + request.json.get('title') + '"'

    template = None
    with open(f"{app_folder}/template.md") as f:
        template = f.read()
    if not template:
        abort(Response("Template open failed", 500))
    date = datetime.isoformat(datetime.now()).split(".")[0]
    tz = time.strftime("%z")
    real_content = template.format(title=title, content=content, date=date+tz)
    filename = f"tools-generated-name-{date}.md"
    generate_file(filename, real_content)
    return make_response("", 202)



