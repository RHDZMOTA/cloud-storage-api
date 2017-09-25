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


db.create_all()
