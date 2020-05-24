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

# @app.route("/api/food")
# def show_foods():
#     res = find_recipes()
#     json_data = json.loads(res.text)
#     print(json_data)
#     return jsonify(json_data)
#
# @app.route("/webhook", methods=["POST"])
# def webhook():
#     req = request.get_json(silent=true, force=True)
#     print("Request: ")
#     print(json.dumps(req, indent=4))
#     res = makeWebhookResult(req)
#     res = json.dumps(res, indent=4)
#     print(res)
#     r = make_response(res)
#     r.headers["Content-Type"] = 'application/json'
#     return r
#
# def makeWebhookResult(req):
#     if req.get("result").get("action") != "recipes":
#         return {}
#     result = req.get("result")
#     parameters = result.get("parameters")
#     zone = parameters.get("ingredients")
#     speech = "The food I can recommend you is" + zone + ", ok?"
#     print("response: ")
#     print(speech)
#     return {
#         "speech": speech,
#         "displayText": speech,
#         "source": "ingredients"
#     }


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
