from voiture import Voiture
from crud_db import ajouter_voiture, supprimer_voiture, recuperer_voitures, connecter_db,modifier_voiture


def vider_table_voiture():
    connexion = connecter_db()

    if connexion is None:
        print("Connexion impossible à la base de données.")
        return

    curseur = connexion.cursor()
    curseur.execute("""
        CREATE TABLE IF NOT EXISTS voiture (
            id INT AUTO_INCREMENT PRIMARY KEY,
            marque VARCHAR(100) NOT NULL,
            modele VARCHAR(100) NOT NULL,
            annee INT NOT NULL,
            prix DECIMAL(10, 2) NOT NULL
        )
    """)
    curseur.execute("TRUNCATE TABLE voiture")

    connexion.commit()
    curseur.close()
    connexion.close()

    print("Table voiture vidée.\n")


def afficher_liste_voitures(titre, liste_voitures):
    print(titre)
    print("-" * 40)

    if not liste_voitures:
        print("Aucune voiture trouvée.")
    else:
        for voiture in liste_voitures:
            voiture.afficher_voiture()
            print("-" * 40)

    print()


def main():
    vider_table_voiture()

    v1 = Voiture("Honda", "Civic", 2022, 22000)
    v2 = Voiture("Volkswagen", "Jetta", 2021, 21000)
    v3 = Voiture("Nissan", "Versa", 2020, 17000)
    v4 = Voiture("Audi", "A3", 2023, 32000)

    ajouter_voiture(v1)
    ajouter_voiture(v2)
    ajouter_voiture(v3)
    ajouter_voiture(v4)

    voitures = recuperer_voitures()
    afficher_liste_voitures("Liste des voitures après ajout :", voitures)

    supprimer_voiture(3)
    voiture_modifiee = Voiture("Volkswagen", "Jetta GLI", 2024, 29500, 2)
    modifier_voiture(voiture_modifiee)
    voitures = recuperer_voitures()
    afficher_liste_voitures("Liste des voitures après suppression :", voitures)


if __name__ == "__main__":
    main()