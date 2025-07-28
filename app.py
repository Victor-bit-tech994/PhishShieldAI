from flask import Flask, render_template, request
import joblib
import re

app = Flask(__name__)

# Simulated model (for showcase purposes)
def is_phishing(url):
    return "phish" in url.lower()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    url = request.form['url']
    result = "Phishing Detected!" if is_phishing(url) else "Looks Safe ✅"
    return render_template('index.html', url=url, result=result)

if __name__ == '__main__':
    app.run(debug=True)
