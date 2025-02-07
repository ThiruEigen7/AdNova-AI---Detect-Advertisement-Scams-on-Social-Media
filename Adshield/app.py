from flask import Flask, render_template, request
import random  
from loader import url_loader
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect():
    data = request.get_json()
    url = data.get("url", "")
    #scrap = url_loader(url) # loader function
    #img = scrap[1]

    # prediction

    #result = ad_predict(img)
    result = 0
    if result > 0.5:
      scam_result = 'Spam'
    else:
      scam_result = 'Verified'

    return jsonify({"result": scam_result})


@app.route("/ad-scam")
def ad_scam():
    return render_template("index.html")

@app.route("/user-profiling")
def user_profiling():
    return render_template("user_profiling.html")

@app.route("/phishing")
def phishing():
    return render_template("phishing.html")



if __name__ == "__main__":
    app.run(debug=True)
