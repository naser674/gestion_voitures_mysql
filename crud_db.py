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