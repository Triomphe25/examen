class Medicament:
    
    def __init__(self, id_medicament, nom, quantite_stock):
        self.__id_medicament = id_medicament
        self.__nom = nom
        self.__quantite_stock = quantite_stock
        
    def afficher_infos(self):
        print(f"Médicament : {self.__nom}, Stock : {self.__quantite_stock}")

    # Getter pour 'nom'
    def get_nom(self):
        return self.__nom

class MedicamentPerissable(Medicament):
    def afficher_infos(self):
        print(f"[PÉRISSABLE] {self.get_nom()} - Attention à la date d'expiration !")

class MedicamentNonPerissable(Medicament):
    def afficher_infos(self):
        print(f"[NON PÉRISSABLE] {self.get_nom()} - Stock stable.")

medicament1 = MedicamentPerissable(1, "Paracétamol", 25)
medicament1.afficher_infos()
