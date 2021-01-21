from mongoengine import Document, StringField, DateTimeField, FloatField
from flask_mongoengine.wtf import model_form

from etc.utcTimeStamp import get_utc_time_stamp

class General_settings(Document):
	name = StringField(required=True, max_length=100)
	logo = StringField(required=True)
	slider = StringField(required=True)
	text = StringField(required=True)
	last_actualization = FloatField(required=True, default=get_utc_time_stamp())

class Actions(Document):
	name = StringField(required=True, max_length=100)
	date = FloatField(required=True)
	photo = StringField(required=True)
	text = StringField(required=True)

class News(Document):
	name = StringField(required=True, max_length=100)
	photo = StringField(required=False)
	text = StringField(required=True)
	date = DateTimeField(required=True)

