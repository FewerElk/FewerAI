# FewerAI | src.fewerai.__init__.py
# This file is ruled by the license joined.

import requests

class AccessForbiddenException(Exception):
    """Raised when failed to login to the API server."""
    pass

class BadRequestException(Exception):
    """Raised when the server can't decode the request."""
    pass

class ServiceUnavailableException(Exception):
    """Raised when the server get an internall exceptio, or when the server is not reachable."""

class AccountBannedException(Exception):
    """Raised when the provided account is suspended."""

class SessionNotFoundException(Exception):
    """Raised when the serveur can't find the requested session."""

class API(object):
    def __init__(self, username:str, token:str):
        self.username = username
        self.token = token
        
    def generate(self, request:str) -> str:
        """Uses the FewerAI API to generate a text"""
        try:
            data = "{}%{}%{}".format(self.username, self.token, request)


            url = "http://n1.recloud-hosting.me:1123/api"

            response = requests.post(url, data=data)

            if response.text == "400":
                raise BadRequestException("Bad Request. Please update the version of this client or post an issue here : https://github.com/FewerElk/FewerAI/issues")
            elif response.text == "403":
                raise AccessForbiddenException("Failed to login: incorrect username or password.")
            elif response.text == "403-B":
                try:
                    raise AccountBannedException("The provided credentials are suspended by the server.")
                except AccountBannedException as e:
                    raise AccessForbiddenException("Could not log in to the server.") from e

            elif response.text == "503":
                raise ServiceUnavailableException("An internal exception occured when performing the generation. Maybe the server couldn't decode your request. Did you used utf-8 caracters ?")
            else:
                return response.text
        except requests.exceptions.ConnectionError:
            raise ServiceUnavailableException("Could not connect to the server. Please open an issue.")
        
    def create_session(self, request:str) -> dict:
        """Create a session (=discussion) that use your old message. Return {"sessionid", "response"}."""
        try:
            data = "{}%{}%{}%{}".format(self.username, self.token, 1, request)

            # URL de l'API Flask
            url = "http://n1.recloud-hosting.me:1123/api/session"

            response = requests.post(url, data=data)

            if response.text == "400":
                raise BadRequestException("Bad Request. Please update the version of this client or post an issue here : https://github.com/FewerElk/FewerAI/issues")
            elif response.text == "403":
                raise AccessForbiddenException("Failed to login: incorrect username or password.")
            elif response.text == "403-B":
                try:
                    raise AccountBannedException("The provided credentials are suspended by the server.")
                except AccountBannedException as e:
                    raise AccessForbiddenException("Could not log in to the server.") from e

            elif response.text == "503":
                raise ServiceUnavailableException("An internal exception occured when performing the generation. Maybe the server couldn't decode your request. Did you used utf-8 caracters ?")
            else:
                resp, sessionid = response.text.split("%")
                return {"sessionid": sessionid, "response": resp}
        except requests.exceptions.ConnectionError:
            raise ServiceUnavailableException("Could not connect to the server. Please open an issue.")
        
    def generate_with_session(self, request:str, sessionID: str) -> str:
        """use a session (=discussion) that use your old message to generate a text."""
        try:
            data = "{}%{}%{}%{}%{}".format(self.username, self.token, 2, request, sessionID)


            url = "http://n1.recloud-hosting.me:1107/api/session"

            response = requests.post(url, data=data)

            if response.text == "400":
                raise BadRequestException("Bad Request. Please update the version of this client or post an issue here : https://github.com/FewerElk/FewerAI/issues")
            elif response.text == "403":
                raise AccessForbiddenException("Failed to login: incorrect username or password.")
            elif response.text == "403-B":
                try:
                    raise AccountBannedException("The provided credentials are suspended by the server.")
                except AccountBannedException as e:
                    raise AccessForbiddenException("Could not log in to the server.") from e
                
            elif response.text == "404":
                raise SessionNotFoundException(f"The provided session id {sessionID} was not found by the server. To create one, please use API.create_session().")

            elif response.text == "503":
                raise ServiceUnavailableException("An internal exception occured when performing the generation. Maybe the server couldn't decode your request. Did you used utf-8 caracters ?")
            else:
                return response.text
        except requests.exceptions.ConnectionError:
            raise ServiceUnavailableException("Could not connect to the server. Please open an issue.")