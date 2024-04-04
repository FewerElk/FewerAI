# FewerAI | src.fewerai.fewerai.py
# This file is ruled by the BSD 3 Clause license:
"""BSD 3-Clause License

Copyright (c) 2024, FewerElk

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

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
