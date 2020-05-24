import datetime
import json
import os

from flask import Flask, render_template, jsonify, request, redirect
from flask import make_response
from VisionAPI_demo import process_image

from settings import mongo

app = Flask(__name__, static_folder="public")

db = mongo["peterspan"]
collection = db["users"]

app.config['SPOONACULAR_API_KEY'] = os.getenv('SPOONACULAR_API_KEY')

@app.route('/')
def root():
    return render_template('peterpan.html')

@app.route("/profile", methods=["GET", "POST"])
def profile():
    if request.method == "GET":
        return render_template("peterpan-profile.html")
    else:
        username = request.form["name"]
        dietary_restriction = request.form["restriction"]
        allergy = request.form["allergy"]
        health_concerns = request.form["concern"]

        collection.insert_one({
            "name": username,
            "dietary-restriction": dietary_restriction,
            "allergy": allergy,
            "health-concerns": health_concerns
        })
        return redirect("/")

@app.route("/upload", methods=["POST"])
def upload_process():
    if request.files:
        req = request.files["visual"]

        filename = "./images/" + req.filename
        req.save(filename)
        process_image(filename)

        return redirect("https://creator.voiceflow.com/demo/4370061089187153", code=302)
    else:
        response = app.response_class(
            response = json.dumps("error: no image received"),
            status = 400,
            mimetype = "application/json"
        )
        return response


if __name__ == '__main__':
    # app.run(host='127.0.0.1', port=8080, debug=True)
    app.run()
