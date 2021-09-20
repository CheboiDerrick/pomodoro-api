from flask import request
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from app.auth.v1.models.user_model import UserModel

parser = RequestParser()
parser.add_argument("username", type=str, required=True, help="Please input a username")


class User(Resource):
    """
    User endpoints
    """

    def post(self):
        """
        Register a user endpoint
        """
        args = parser.parse_args()
        args = request.get_json()
        username = args["username"]
        password = args["password"]
        task = args["task"]
        tasktime = args["tasktime"]
        break_time = args["break_time"]

        newUser = UserModel(username,password, task, tasktime, break_time)
        newUser.save_user()

        return {
            "message": "Task successfully started",
            "user": newUser.__dict__,
        }, 201

    def get(self):
        """"
        
        """
        return {
            "users":UserModel.users
        }, 200

