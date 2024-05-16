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

