import json
import mysql.connector


def connecter_db():
    try:
        with open("config.json", "r", encoding="utf-8") as fichier:
            config = json.load(fichier)

        connexion = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )

        return connexion

    except FileNotFoundError:
        print("Erreur : le fichier config.json est introuvable.")
    except KeyError as e:
        print(f"Erreur : cle manquante dans config.json : {e}")
    except mysql.connector.Error as e:
        print(f"Erreur de connexion à MySQL : {e}")

    return None
def ajouter_voiture(voiture):
    connexion = connecter_db()

    if connexion is None:
        print("Connexion impossible à la base de données.")
        return

    curseur = connexion.cursor()

    requete_creation = """
    CREATE TABLE IF NOT EXISTS voiture (
        id INT AUTO_INCREMENT PRIMARY KEY,
        marque VARCHAR(100) NOT NULL,
        modele VARCHAR(100) NOT NULL,
        annee INT NOT NULL,
        prix DECIMAL(10, 2) NOT NULL
    )
    """
    curseur.execute(requete_creation)

    requete_insertion = """
    INSERT INTO voiture (marque, modele, annee, prix)
    VALUES (%s, %s, %s, %s)
    """
    valeurs = (voiture.marque, voiture.modele, voiture.annee, voiture.prix)
    curseur.execute(requete_insertion, valeurs)

    connexion.commit()
    curseur.close()
    connexion.close()

    print("Voiture ajoutée avec succès.")
def supprimer_voiture(id):
    connexion = connecter_db()

    if connexion is None:
        print("Connexion impossible à la base de données.")
        return

    curseur = connexion.cursor()

    requete = "DELETE FROM voiture WHERE id = %s"
    curseur.execute(requete, (id,))

    connexion.commit()
    curseur.close()
    connexion.close()

    print("Voiture supprimée avec succès.")

def recuperer_voitures():
    connexion = connecter_db()

    if connexion is None:
        print("Connexion impossible à la base de données.")
        return []

    curseur = connexion.cursor()
    requete = "SELECT id, marque, modele, annee, prix FROM voiture"
    curseur.execute(requete)

    resultats = curseur.fetchall()
    liste_voitures = []

    from voiture import Voiture
    for ligne in resultats:
        voiture = Voiture(
            marque=ligne[1],
            modele=ligne[2],
            annee=ligne[3],
            prix=ligne[4],
            id=ligne[0]
        )
        liste_voitures.append(voiture)

    curseur.close()
    connexion.close()

    return liste_voitures