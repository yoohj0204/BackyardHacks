import datetime
import json
import os

from flask import Flask, render_template, jsonify, request
from flask import make_response

app = Flask(__name__, static_folder="public")
app.config['SPOONACULAR_API_KEY'] = os.getenv('SPOONACULAR_API_KEY')

@app.route('/')
def root():
    return render_template('macaroni-laboratory.html')

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
