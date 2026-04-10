from crud_db import connecter_db,ajouter_voiture,supprimer_voiture
from voiture import Voiture

connexion = connecter_db()

if connexion is not None:
    print("Connexion réussie")
    connexion.close()
else:
    print("La connexion a échoué")


v1 = Voiture("Honda", "Civic", 2022, 22000)
v2 = Voiture("Volkswagen", "Jetta", 2021, 21000)
v3 = Voiture("Nissan", "Versa", 2020, 17000)
v4 = Voiture("Audi", "A3", 2023, 32000)

ajouter_voiture(v1)
ajouter_voiture(v2)
ajouter_voiture(v3)
ajouter_voiture(v4)

def main():
    supprimer_voiture(2)

if __name__ == "__main__":
    main()
