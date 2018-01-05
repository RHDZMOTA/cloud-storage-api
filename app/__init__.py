from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('app_config')

db = SQLAlchemy(app)


#@app.error_handlers(404)
#def not_found(error):
#    return render_template('404.html'), 404

from app.mod_temporal_link.controllers import mod_temporal_link as temporal_link
app.register_blueprint(temporal_link)

from app.mod_cv.controller import mod_cv as cv
app.register_blueprint(cv)

from app.mod_upload_file.controllers import mod_upload_file as upload_file
app.register_blueprint(upload_file)

from app.mod_cloud_vision.controllers import mod_cloud_vision as cloud_vision
app.register_blueprint(cloud_vision)


db.create_all()
