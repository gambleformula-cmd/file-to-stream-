from flask import Flask, render_template, redirect
from config import SECRET_KEY, ACTIVE_BOT_URL
from data.courses import COURSES
import os

app = Flask(__name__)
app.secret_key = SECRET_KEY

@app.route("/")
def index():
    return render_template("index.html", courses=COURSES)

@app.route("/get-access")
def get_access():
    # 🔥 SINGLE REDIRECT POINT
    return redirect(ACTIVE_BOT_URL)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
