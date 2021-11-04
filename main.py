from flask import Flask, request, jsonify, send_file
import werkzeug.utils as w
import os
from db_conn import DBConnection


app = Flask(__name__)

db = DBConnection()

@app.route("/", methods=["GET"])
def test():
    return jsonify({"Message": "OK"})


@app.route("/upload", methods=["POST"])
def upload():
    if request.method == "POST":
        imagefile = request.files["image"]
        filename = w.secure_filename(imagefile.filename)
        imagefile.save("./images/" + filename)
        return jsonify({"message": "Image uploaded successfully"})


@app.route("/image/<name>", methods=["GET"])
def image(name):
    image = os.path.join(f"images/{name}")
    return send_file(image, mimetype='image/png')


if __name__ == "__main__":
    app.run()
