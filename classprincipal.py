class Medicament:
    
    # encapsulation
    def __init__(self, id_medicament, nom, quantite_stock):
        self.__id_medicament = id_medicament
        self.__nom = nom
        self.__quantite_stock = quantite_stock
        
    # Méthode principale
    def afficher_infos(self):
        print(f"Médicament : {self.__nom}, Stock : {self.__quantite_stock}")

# Création d'un médicament avec les bons paramètres
medicament1 = Medicament(1, "Paracétamol", 25)
medicament1.afficher_infos()
