import requests

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
        raise Exception("Bad Request")
    elif response.text == "403:
        raise Exception("Bad Token")
    # Affichage de la réponse du serveur
    return response.text
