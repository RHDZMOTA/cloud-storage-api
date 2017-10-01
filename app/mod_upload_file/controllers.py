from flask import Blueprint, request, render_template, jsonify
from app import db

import util
import settings.config as config

mod_upload_file = Blueprint('upload-file', __name__, url_prefix='/upload-file')


@mod_upload_file.route('/', methods=['GET', 'POST'])
def get_index():
    print("SHOW INDEX")
    return render_template('upload-file/index.html')


@mod_upload_file.route('/dropbox', methods=['POST'])
def dropbox_upload():

    file_name = request.form.get("file_name")
    file_path = request.form.get("file_path")
    file_contents = request.files.get('file')

    if file_contents is None:
        return render_template("upload-file/dropbox_usage.html")

    drop_box = util.DropboxHandler(config=config.DropboxConfig)
    drop_box.upload_file_contents(
        upload_path=file_path if file_path else "",
        upload_file_name=file_name,
        file_contents=file_contents.read()
    )

    return jsonify({
        "status": True,
        "file_contents": str(file_contents.read()),
        "upload_file_name": file_name,
        "upload_path": file_path if file_path else ""
    })


@mod_upload_file.route('/dropbox', methods=['GET'])
def dropbox_upload_by_url():

    file_name = request.args.get("file_name")
    file_path = request.args.get("file_path")
    file_url = request.args.get("file_url")
    upload_file_path = request.args.get("upload_file_path")

    if file_url is None:
        return "file_url is None."

    file_info = util.file_operations.download_file(
        file_url=file_url,
        file_name=file_name,
        file_path=file_path
    )

    drop_box = util.DropboxHandler(config=config.DropboxConfig)
    drop_box.upload_file_contents(
        upload_path=upload_file_path if upload_file_path is not None else "",
        upload_file_name=file_name if file_name is not None else "file",
        file_contents=file_info.get("file_contents")
    )

    return jsonify({
        "status": True,
        "file_contents": str(file_info.get("file_contents")),
        "upload_file_name": file_name if file_name is not None else "file",
        "upload_path": upload_file_path if upload_file_path else "",
        "from_file": (file_path + "/" if file_path else "") + file_name
    })


