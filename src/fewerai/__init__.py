# FewerAI | src.fewerai.__init__.py
# This file is ruled by the license joined.

import requests

class LoginException(Exception):
    """Raised when failed to login to the API server."""
    pass

class BadRequestException(Exception):
    """Raised when the server can't decode the request."""
    pass

class ServiceUnavailableException(Exception):
    """Raised when the server get an internall exceptio, or when the server is not reachable"""

class API(object):
    def __init__(self, username:str, token:str):
        self.username = username
        self.token = token
        
    def generate(self, request:str):
        """Uses the FewerAI API to generate a text"""
        try:
            data = "{}%{}%{}".format(self.username, self.token, request)

            # URL de l'API Flask
            url = "http://n1.recloud-hosting.me:1123/api"

            response = requests.post(url, data=data)

            if response.text == "400":
                raise BadRequestException("Bad Request. Please update the version of this client or post an issue here : https://github.com/FewerElk/FewerAI/issues")
            elif response.text == "403":
                raise LoginException("Failed to login: incorrect username or password.")
            elif response.text == "503":
                raise ServiceUnavailableException("An internal exception occured when performing the generation. Maybe the server couldn't decode your request. Did you used utf-8 caracters ?")
            else:
                return response.text
        except requests.exceptions.ConnectionError:
            raise ServiceUnavailableException("Could not connect to the server. Please open an issue.")