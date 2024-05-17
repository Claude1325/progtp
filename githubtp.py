'''
Votre description du programme
@auteur(e)s     Claude Bernard Lucien
@matricules     e2236254
@date              20-05-2024
'''



import csv
import json
import math
class DonneesGeo:
    def __init__(self, ville, pays, latitude, longitude):
        self.ville = str(ville)
        self.pays = str(pays)
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def __str__(self):
        return f"Ville: {self.ville}, Pays: {self.pays}, Latitude: {self.latitude}, Longitude: {self.longitude}"
def lireDonneesCsv(nom_fichier):
    donnees_geo = []
    with open(nom_fichier, 'r', encoding='utf-8') as fichier:
        lecteur_csv = csv.reader(fichier)
        next(lecteur_csv)  # Ignorer la première ligne (en-têtes)
        for ligne in lecteur_csv:
            ville, pays, latitude, longitude = ligne
            donnees = DonneesGeo(ville.strip(), pays.strip(), float(latitude), float(longitude))
            donnees_geo.append(donnees)
    return donnees_geo
#deuxieme partie a etre push
    nom_fichier_csv = "data.csv"
    donnees_geo = lireDonneesCsv(nom_fichier_csv)

    # Afficher les données géographiques lues à partir du fichier CSV
    for donnees in donnees_geo:
        print(donnees)
def ecrireDonneesJson(DATA, donnees_geo):
    # Convertir la liste d'objets DonneesGeo en une liste de dictionnaires
    donnees_dict = []
    for donnees in donnees_geo:
        donnees_dict.append({
            'ville': donnees.ville,
            'pays': donnees.pays,
            'latitude': donnees.latitude,
            'longitude': donnees.longitude
        })

    # Écrire la liste de dictionnaires dans le fichier JSON
    with open(DATA, 'w', encoding='utf-8') as fichier:
        json.dump(donnees_dict, fichier, ensure_ascii=False, indent=4)

# Exemple d'utilisation de la fonction ecrireDonneesJson

    # Supposons que vous avez une liste d'objets DonneesGeo
    donnees_geo = [
        DonneesGeo("Paris", "France", 48.8534951, 2.3483915),
        DonneesGeo("Londres", "Angleterre", 51.5073219, -0.1276474),
        # Ajoutez d'autres objets DonneesGeo selon vos besoins
    ]

    # Utilisez le nom de votre fichier JSON approprié ici
    nom_fichier_json = "DATA.json"
    ecrireDonneesJson(nom_fichier_json, donnees_geo)


def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Rayon de la Terre en kilomètres
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return d

# Coordonnées de Londres (Royaume-Uni) et Hong Kong (Chine)
ville1_nom = "Londres"
ville1_pays = "Angleterre"
ville1_lat = 51.5073219
ville1_lon = -0.1276474

ville2_nom = "Hong Kong"
ville2_pays = "Chine"
ville2_lat = 22.2793278
ville2_lon = 114.1628131

# Calcul de la distance
distance = haversine(ville1_lat, ville1_lon, ville2_lat, ville2_lon)

# Affichage des informations
print(f"Distance minimale en kilomètres entre 2 villes : Ville 1 : {ville1_nom}, Pays : {ville1_pays}, Latitude : {ville1_lat}, Longitude : {ville1_lon} et Ville 2 : {ville2_nom}, Pays : {ville2_pays}, Latitude : {ville2_lat}, Longitude : {ville2_lon}.")
print(f"Distance en kilomètres : {distance}")

# Sauvegarde dans le fichier CSV
with open('distances.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ville1', 'ville2', 'distance'])
    writer.writerow([ville1_nom, ville2_nom, distance])



# Fonction pour calculer la distance entre deux points en utilisant la formule de Haversine
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Rayon de la Terre en kilomètres
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) * math.cos(
        math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c
    return d