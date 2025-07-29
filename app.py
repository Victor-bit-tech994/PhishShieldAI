from flask import Flask, render_template, request
import re
import os

app = Flask(__name__)

def is_phishing(url):
    phishing_keywords = ["login", "verify", "update", "secure", "banking"]
    if any(word in url.lower() for word in phishing_keywords):
        return True
    if not re.match(r'^https://', url):
        return True
    return False

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        url = request.form["url"]
        result = "Phishing Link Detected" if is_phishing(url) else "Safe Link"
    return render_template("index.html", result=result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
