import requests

def send_request(username, password, user_request):
    # Formatage des données dans le format spécifié
    data = "{}%{}%{}".format(username, password, user_request)
    
    # URL de l'API Flask
    url = "http://n1.recloud-hosting.me:1123/api"
    
    # Envoi de la requête POST avec les données au serveur
    response = requests.post(url, data=data)
    
    # Affichage de la réponse du serveur
    print(response.text)

if __name__ == '__main__':
    # Exemple d'utilisation
    username = "username"
    password = "password"
    user_request = "requete"
    send_request(username, password, user_request)
