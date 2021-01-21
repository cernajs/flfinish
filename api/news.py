from flask import jsonify, request, Response
from flask_restful import Resource


from models.parts import News
from etc.utcTimeStamp import get_utc_time_stamp

timestamp = get_utc_time_stamp()

update_dict = {
    "set__last_actualization" : timestamp
}

class NewsApi(Resource):
    def get(self, news_id) -> Response:
        output = News.objects.get(id=news_id)
        return jsonify({'result': output})

    def put(self, news_id) -> Response:
        data = request.get_json()
        put_data = News.objects(id=news_id).update(**data)
        return jsonify({"result": put_data})

    def delete(self, news_id) -> Response:
        out = News.objects(id=news_id).delete()
        return jsonify({"result": out})

class NewsPostApi(Resource):
    def post(self) -> Response:
        data = request.get_json()
        post_data = News(**data, **update_dict).save()
        out = {"id" : str(post_data.id)}
        return jsonify({"result":out})