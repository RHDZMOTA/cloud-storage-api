from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify
from werkzeug import check_password_hash, generate_password_hash
from app import db
from app.mod_temporal_link.models import User

import util
import settings.config as config

mod_temporal_link = Blueprint('temporal-link', __name__, url_prefix='/temporal-link')


@mod_temporal_link.route('/', methods=['GET', 'POST'])
def get_index():
    print("SHOW INDEX")
    return render_template('temporal_link/index.html')


@mod_temporal_link.route('/a-word/<word>', methods=['GET', 'POST'])
def get_word(word=None):
    return jsonify({
        "word": word
    })


@mod_temporal_link.route('/dropbox-files', methods=['GET'])
def dropbox_files():

    file_name = request.args.get("file_name")
    file_path = request.args.get("file_path")

    if file_name is None:
        return render_template("temporal_link/dropbox_usage.html")

    drop_box = util.DropboxHandler(config=config.DropboxConfig)
    file_url, file_metadata = drop_box.get_temporal_url(
        file_name=file_name,
        path=file_path if file_path else "")
    return jsonify({
        "complete-filename": ((file_path + "/") if file_path else "") + file_name,
        "filename": file_name,
        "metadata": str(file_metadata),
        "url": file_url
    })



