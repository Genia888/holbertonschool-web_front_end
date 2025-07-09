import requests

# L'URL du fichier vidéo à vérifier
video_url = 'https://intranet-projects-files.s3.amazonaws.com/webstack/BigBuckBunny.mp4'

# Vérifie si l'URL du vidéo est accessible
try:
    response = requests.get(video_url)  # Envoie une requête HTTP
    if response.status_code == 200:
        print("video has correct source")  # Affiche ce message si l'URL est valide
    else:
        print("video source is incorrect or unavailable")  # Affiche un message si l'URL est incorrecte
except requests.exceptions.RequestException as e:
    print(f"Error checking video source: {e}")  # Affiche une erreur en cas de problème réseau
