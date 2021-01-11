from flask import make_response, request
from flask_restful import Resource

from app.api.v1.user.service import UserService
from app.api.v1.user.service import AccountService, AuthService, DuplicateCheck




class User(Resource):
    def get(self, username):
        return make_response(UserService.provide_user_info(username))

    def patch(self, username):
        return make_response(UserService.modify_user_info(username, request.json))

class Account(Resource):
    def get(self):
        return make_response(AccountService.provide_account_info())

    def post(self):
        return make_response(AccountService.register_account(request.json))

    def delete(self):
        return make_response(AccountService.delete_account(request.args.get('email')))

class AccountPassword(Resource):
    def put(self):
        return make_response(AccountService.change_account_password(request.json))

class Auth(Resource):
    def post(self):
        return make_response(AuthService.login(request.json))

class Refresh(Resource):
    def get(self):
        return make_response(AuthService.refresh())

class DuplicateCheckEmail(Resource):
    def get(self):
        return make_response(DuplicateCheck.email_check(request.args.get('email')))

class DuplicateCheckUsername(Resource):
    def get(self):
        return make_response(DuplicateCheck.username_check(request.args.get('username')))

class AuthEmailVerificationCode(Resource):
    def post(self):
        return make_response(AccountService.verify_email_verification_code(verification_code=request.args.get('verification-code')))
