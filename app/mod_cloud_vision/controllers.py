from flask import Blueprint, request, render_template, jsonify
from app import db

import util
import settings.config as config

mod_cloud_vision = Blueprint('cloud-vision', __name__, url_prefix='/cloud-vision')


@mod_cloud_vision.route('/', methods=['GET', 'POST'])
def get_index():
    print("SHOW INDEX")
    return "hey"#render_template('cloud_vision/index.html')


@mod_cloud_vision.route('/google-dropbox-ocr', methods=['GET', "POST"])
def apply_ocr_for_image_url():

    file_url = request.args.get("file_url") if request.method == "GET" else request.get_json().get("file_url")

    if file_url is None:
        return render_template('cloud_vision/cloud_vision_usage.html')

    detected_text = util.OCR.get_text_from_url(file_url)

    return jsonify({
        "original-url": file_url,
        "temporal-url": "not-available",
        "text": detected_text
    })
