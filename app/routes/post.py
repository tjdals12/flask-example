from flask import Blueprint
from flask_restful import Api
from resources.post import PostListController, PostController

post_blueprint = Blueprint("posts", __name__, url_prefix="/posts")
post_blueprint_api = Api(post_blueprint)

post_blueprint_api.add_resource(PostListController, "/")
post_blueprint_api.add_resource(PostController, "/<int:post_id>")
