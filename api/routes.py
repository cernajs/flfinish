from api.setting import SettingsApi
from api.actions import ActionsApi, ActionApi
from api.news import NewsApi, NewsPostApi
from flask_expects_json import expects_json

from url_validate.resource_validate import *

def create_routes(api):
    api.add_resource(SettingsApi, '/general-settings/<setting_id>')
    api.add_resource(ActionsApi, '/actions/<action_id>')
    api.add_resource(ActionApi, '/actions/')
    api.add_resource(NewsApi, '/news/<news_id>')
    api.add_resource(NewsPostApi, '/news/')
