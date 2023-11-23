from stub_io import StubIO
from repositories.user_repository import UserRepository
from services.user_service import UserService
from app import App
import re


class AppLibrary:
    def __init__(self):
        self._io = StubIO()
        self._user_repository = UserRepository()
        self._user_service = UserService(self._user_repository)

        self._app = App(
            self._user_service,
            self._io
        )

    def input(self, value):
        self._io.add_input(value)

    def output_should_contain(self, value):
        outputs = self._io.outputs

        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )

    def run_application(self):
        self._app.run()

    def create_user(self, username, password):
        self._user_service.create_user(username, password)
    
    def validate(self, username, password):
        self._user_repository.validate(username, password)
    
    # def validate_username(self, username):
    #     if len(username) < 3:
    #         print("error")
        
    #     if username in self._user_repository.find_all():
    #         print("error")

    #     if re.match("^[a-z]+$", username):
    #         print("ok")
    #     else:
    #         print("error")
    
    # def validate_password(self, password):
    #     if len(password) < 8:
    #         print("error")
        
    #     if re.match("^[a-z]+$", password):
    #         if re.match("^[0-9+$", password):
    #             print("ok")
    #     else:
    #         print("error")

        





