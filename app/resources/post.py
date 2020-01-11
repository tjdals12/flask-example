from flask_restful import Resource, reqparse
from models.post import Post
from models import db

parser = reqparse.RequestParser()
parser.add_argument('content')


class PostListController(Resource):
    def get(self):
        # posts = Post.query.all()
        # posts = Post.query.limit(2).all()
        # posts = Post.query.filter(Post.content.like('%Post%')).all()
        # posts = Post.query.filter_by(content="Post").all()
        posts = Post.query.order_by(Post.id.desc()).all()

        return [dict(post.to_dict()) for post in posts]

    def post(self):
        args = parser.parse_args()
        post = Post(args['content'])
        db.session.add(post)
        db.session.commit()

        return post.to_dict()


class PostController(Resource):
    def get(self, post_id):
        post = Post.query.get(post_id)

        if not post:
            return "Not found", 404

        return post.to_dict()

    def patch(self, post_id):
        post = Post.query.get(post_id)

        post.content = 'Edit Text'
        db.session.commit()

        return post.to_dict()

    def delete(self, post_id):
        post = Post.query.get(post_id)

        db.session.delete(post_id)
        db.session.commit()

        return 202
