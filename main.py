from flask import Flask, request, jsonify, send_file
import werkzeug.utils as w
import os
import random


app = Flask(__name__)


def random_image():
    """
    Return a random image from the ones in the static/ directory
    """
    img_dir = "./images"
    img_list = os.listdir(img_dir)
    img_path = os.path.join(img_dir, random.choice(img_list))
    return img_path


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


@app.route("/random", methods=["GET"])
def image():
    """
    Returns a random image directly through send_file
    """
    image = random_image()
    return send_file(image, mimetype='image/png')


if __name__ == "__main__":
    app.run()
