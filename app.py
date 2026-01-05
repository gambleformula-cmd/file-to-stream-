from flask import Flask, render_template, request, redirect, url_for
from telegram import check_join
from config import SECRET_KEY
import os

app = Flask(__name__)
app.secret_key = SECRET_KEY

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/course")
def course():
    user_id = request.args.get("uid")
    if not user_id:
        return redirect(url_for("lock"))

    if check_join(user_id):
        return redirect("https://t.me/your_private_channel")  # VIDEO
    return redirect(url_for("lock"))

@app.route("/lock")
def lock():
    return render_template("lock.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
