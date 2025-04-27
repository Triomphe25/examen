from datetime import datetime

class Medicament_reference:
    
    # surcharge
    def __init__(self, id_medicament, nom, reference, quantite_stock, date_expiration, prix):
        self.__id_medicament = id_medicament
        self.__nom = nom
        self.__reference = reference
        self.__quantite_stock = quantite_stock
        self.__date_expiration = date_expiration
        self.__prix = prix

    

    # Méthode principale
    def afficher_infos(self):
        print(f"Médicament : {self.nom}, Stock : {self.__quantite_stock}")

    # Surcharge de méthode
    def ajouter(self, nom, quantite, date_expiration=None):
        self.__nom = nom
        self.__quantite_stock = quantite
        self.__date_expiration = date_expiration
