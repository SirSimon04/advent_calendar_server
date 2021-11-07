from flask import Flask, request, jsonify, send_file, Response
import werkzeug.utils as w
import os
from db_conn import DBConnection
import json
import glob

app = Flask(__name__)

db = DBConnection()


@app.route("/", methods=["GET"])
def test():
    return jsonify({"Message": "OK"})


@app.route("/calendar", methods=["POST"])
def create_calendar():
    json = request.get_json()
    db.insert_calendar(json["id"], json["title"], json["msg"], json["from"], json["to"])
    return jsonify({"message": "Image uploaded successfully"})


@app.route("/calendar/<id>", methods=["GET"])
def get_calendar(id):
    result = db.get_calendar(id)

    if not "id" in result:
        resp = Response(json.dumps({"Message": "Nicht gefunden"}), 404, mimetype="application/json")
        return resp

    returnFileNames = [];

    allFileNames = glob.glob("./images/*")

    for fileName in allFileNames:
        dId = fileName.split("/")[2]
        dId = dId.split("_")[0]
        if dId == id:
            returnFileNames.append(fileName.split("/")[2])

    result["fileNames"] = returnFileNames;


    resp = Response(json.dumps(result), 200, mimetype="application/json")
    resp.headers["Access-Control-Allow-Origin"] = "*"

    return resp

@app.route("/image", methods=["POST"])
def upload():
    for i in range(1):
        imagefile = request.files[str(i)]
        filename = w.secure_filename(imagefile.filename)
        imagefile.save("./images/" + filename)
    return jsonify({"message": "Images uploaded successfully"})


@app.route("/image/<name>", methods=["GET"])
def get_image(name):
    image = os.path.join(f"images/{name}")
    return send_file(image, mimetype='image/png')


if __name__ == "__main__":
    app.run()
