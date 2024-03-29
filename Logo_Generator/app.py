import os
from flask import Flask,  request, jsonify, send_from_directory
import test
from gen_data import gen_data
from flask_cors import CORS
from options import get_parser

app = Flask(__name__)
CORS(app)
parser = get_parser()
opts = parser.parse_args()


@app.route("/create", methods=['POST'])
def use_model():
    word = request.json
    print(word)
    print(type(word))
    opts.mode = 'test'
    opts.input_text = word
    # opts.style = 'texture_style/test2-paint.png'
    # opts.style_sem = 'texture_style/test2-sem.png'
    opts.style = 'texture_style/glyh-paint.png'
    opts.style_sem = 'texture_style/glyh-sem.png'
    opts.experiment_name = opts.experiment_name
    gen_data(opts)
    print(f"Testing on experiment {opts.experiment_name}...")
    test.test(opts)
    return jsonify({"message": "successful cycle"}), 200


@app.route("/results/<filename>", methods=['GET'])
def get_image(filename):
    try:
        return send_from_directory("./outputs", filename, as_attachment=True)
    except FileNotFoundError:
        return jsonify({"error": "Image not found"}), 404


if __name__ == "__main__":
    app.run(debug=True, port=8000)
