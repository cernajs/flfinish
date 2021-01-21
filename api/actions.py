from flask import jsonify, request, Response
from flask_restful import Resource

from models.parts import Actions
from etc.utcTimeStamp import get_utc_time_stamp
from etc.errors import *

now = get_utc_time_stamp()

class ActionsApi(Resource):
    def get(self, action_id) -> Response:
        output = Actions.objects.get(id=action_id)
        return jsonify({'result': output})

    def put(self, action_id) -> Response:
    	data = request.get_json()
    	if "date" in data:
    		if data["date"] < now:
    			return 401
    	put_data = Actions.objects(id=action_id).update(**data)
    	return jsonify({"result": put_data})

    def delete(self, action_id) -> Response:
    	out = Actions.objects(id=action_id).delete()
    	return jsonify({"result": out})

class ActionApi(Resource):
	def post(self) -> Response:
		data = request.get_json()
		if "date" in data:
			if data["date"] < now:
				return 401
		post_data = Actions(**data).save()
		out = {"id" : str(post_data.id)}
		return jsonify({"result":out})