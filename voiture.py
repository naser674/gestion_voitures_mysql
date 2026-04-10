class Voiture:
    def __init__(self, marque, modele, annee, prix, id=None):
        self.id = id
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def afficher_voiture(self):
        print(f"ID : {self.id}")
        print(f"Marque : {self.marque}")
        print(f"Modèle : {self.modele}")
        print(f"Année : {self.annee}")
        print(f"Prix : {self.prix}$")