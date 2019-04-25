#! env/bin/python3.6
# -*- coding: utf8 -*-

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
#from flask_thumbnails import Thumbnail


app = Flask(__name__)
app.config.from_object('config')

cors = CORS(app)
db = SQLAlchemy(app)
migrate = Migrate (app, db)
ma = Marshmallow(app)

#thumb = Thumbnail(app)


from app import views, models

#from app.API.views import API as api_module
#from app.authentication.views import authentication as authentication_module
#from app.admin.views import administration as admin_module
#from app.kartoteka.views import kartoteka as kartoteka_module
#from app.zal.views import zal as zal_module
#from app.inventory.views import inventory as inventory_module
#from app.CA.views import CA as CA_module

#app.register_blueprint(api_module)
#app.register_blueprint(authentication_module)
#app.register_blueprint(admin_module)
#app.register_blueprint(kartoteka_module)
#app.register_blueprint(zal_module)
#app.register_blueprint(CA_module)
#app.register_blueprint(inventory_module)
