from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from app import db
from app.mod_temporal_link.models import User

import util
import settings.config as config

mod_temporal_link = Blueprint('temporal-link', __name__, url_prefix='/temporal-link')


@mod_temporal_link.route('/', methods=['GET', 'POST'])
def get_index():
    return render_template('temporal_link/index.html')


@mod_temporal_link.route('/dropbox-files/<complete_file_name>', methods=['GET', 'POST'])
def dropbox_files(complete_file_name=None):

    if complete_file_name is None:
        return "Whoa."

    drop_box = util.DropboxHandler(config=config.DropboxConfig)
    return drop_box.get_temporal_url(file_name=complete_file_name, path="")



