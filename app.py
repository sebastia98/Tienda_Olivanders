from flask import Flask
from logica import generar_html_items, gilded_rose, anadir_item

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    html = generar_html_items(gilded_rose.get_items())
    html += "<a href=\"http://127.0.0.1:5000/update\">update</a>"
    return html

@app.route("/update")
def update():
    gilded_rose.update_quality()
    return index()

@app.route("/anadir/<item>/<sellin>/<quality>")
def anadir(item, sellin, quality):
    anadir_item(item, sellin, quality)
    return index()