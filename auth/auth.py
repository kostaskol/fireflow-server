from werkzeug.security import generate_password_hash, check_password_hash
from db import DatabaseConnector

class Auth:
    __instance = None
    @staticmethod
    def get_instance():
        if Auth.__instance is None:
            Auth()
        return Auth.__instance
    
    def __init__(self):
        if Auth.__instance is not None:
            # TODO: Make this an app specific error
            raise Exception("Singleton class already instantiated")
        else:
            Auth.__instance = self
    
    def authenticate(self, username, password):
        user = DatabaseConnector.get_instance().get_user(username)
        return check_password_hash(user['password'], password)

    def sign_up(self, username, password, first_name, last_name):
        # TODO: Add checks
        user = {
            'username': username,
            'password': password,
            'firstName': first_name,
            'lastName': last_name
        }

        DatabaseConnector.get_instance().insert_user(user)