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

# Fonction pour lire les données du fichier CSV et les afficher à l'écran
def lire_et_afficher_csv():
    print("Lecture des données du fichier data.csv...")
    with open('data.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
    input("Appuyez sur Entrée pour revenir au menu.")


# Fonction pour sauvegarder les données dans un fichier JSON
def sauvegarder_dans_json():
    print("Sauvegarde des données dans un fichier JSON...")
    with open('donnees.json', 'w') as jsonfile:
        # Lire les données du fichier CSV
        data = []
        with open('data.csv', 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
        # Écrire les données dans un fichier JSON
        json.dump(data, jsonfile)
    print("Les données ont été sauvegardées dans le fichier donnees.json.")


# Fonction pour lire les données du fichier JSON, les calculs dans le fichier distances.csv
def lire_et_traiter_json():
    print("Lecture des données du fichier JSON...")
    with open('DATA.json', 'r') as jsonfile:
        data = json.load(jsonfile)

    # Calcul des distances et recherche de la distance minimale
    distances = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            ville1 = data[i]
            ville2 = data[j]
            distance = haversine(float(ville1['latitude']), float(ville1['longitude']), float(ville2['latitude']),
                                 float(ville2['longitude']))
            distances.append({'ville1': ville1['ville'], 'ville2': ville2['ville'], 'distance': distance})

    min_distance = min(distances, key=lambda x: x['distance'])

    # Afficher les informations sur la distance minimale
    print(
        f"Distance minimale en kilomètres entre 2 villes : Ville 1 : {min_distance['ville1']}, Ville 2 : {min_distance['ville2']}, Distance en kilomètres : {min_distance['distance']}")

    # Sauvegarde dans le fichier CSV
    with open('distances.csv', 'w', newline='') as csvfile:
        fieldnames = ['ville1', 'ville2', 'distance']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(distances)
    print("Les calculs de distances ont été sauvegardés dans le fichier distances.csv.")


# Fonction principale pour afficher le menu et gérer les options
def afficher_menu():
    while True:
        print("\nMenu :")
        print("1- Lire les données du fichier csv, créer les objets et afficher les données.")
        print("2- Sauvegarder les données dans un fichier .json.")
        print(
            "3- Lire les données du fichier .json, déterminer et afficher les données associées à la distance minimale entre deux villes et sauvegarder les calculs dans distances.csv.")
        print("Entrez un numéro pour choisir une option ou appuyez sur 'q' pour quitter :")

        choix = input()

        if choix == '1':
            lire_et_afficher_csv()
        elif choix == '2':
            sauvegarder_dans_json()
        elif choix == '3':
            lire_et_traiter_json()
        elif choix.lower() == 'q':
            print("Programme terminé.")
            break
        else:
            print("Choix invalide. Veuillez entrer une option valide.")


# Exécution du programme
afficher_menu()