from flask import jsonify, request, Response
from flask_restful import Resource


from models.parts import General_settings
from etc.utcTimeStamp import get_utc_time_stamp

timestamp = get_utc_time_stamp()

update_dict = {
	"set__last_actualization" : timestamp
}

class SettingsApi(Resource):
    def get(self, setting_id) -> Response:
        output = General_settings.objects.get(id=setting_id)
        return jsonify({'result': output})
       

    def put(self, setting_id) -> Response:
    	data = request.get_json()
    	print(data)
    	put_data = General_settings.objects(id=setting_id).update(**data, **update_dict)
    	return jsonify({"result": put_data})
