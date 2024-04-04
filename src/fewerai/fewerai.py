# FewerAI | src.fewerai.fewerai.py
# This file is ruled by the license joined.

import requests

class LoginException(Exception):
    """Raised when failed to login to the API server."""
    pass

class BadRequestException(Exception):
    """Raised when the server can't decode the request."""
    pass

class API(object):
    def __init__(self, username:str, token:str):
        self.username = username
        self.token = token
        
    def generate(self, request:str):
        """Uses the FewerAI API to generate a text"""
        # Formatage des données dans le format spécifié
        data = "{}%{}%{}".format(self.username, self.token, request)

        # URL de l'API Flask
        url = "http://n1.recloud-hosting.me:1123/api"

        # Envoi de la requête POST avec les données au serveur
        response = requests.post(url, data=data)

        if response.text == "400":
            raise BadRequestException("Bad Request. Please update the version of this client or post an issue here : https://github.com/FewerElk/FewerAI/issues")
        elif response.text == "403":
            raise LoginException("Failed to login: incorrect username or password.")
        # Affichage de la réponse du serveur
        return response.text
