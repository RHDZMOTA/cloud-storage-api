from flask import Blueprint, send_file
from app import db

import settings.config as config
mod_cv = Blueprint('cv', __name__, url_prefix='/cv')


@mod_cv.route('/', methods=['GET', 'POST'])
def get_cv():
    return send_file(config.STATIC_DIR + '/docs/CV_R.pdf')
    #with open(config.STATIC_DIR + '/docs/CV_R.pdf', 'rb') as static_file:
    #    return send_file(static_file, attachment_filename='CV_R.pdf')
