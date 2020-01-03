from flask_restful import Resource
from models.post import Post


class PostListController(Resource):
    def get(self):
        posts = Post.query.all()

        return [dict(post.to_dict()) for post in posts]


class PostController(Resource):
    def get(self, post_id):
        post = Post.query.get(post_id)

        if not post:
            return "Not found", 404

        return post.to_dict()
