from crud_db import connecter_db

connexion = connecter_db()

if connexion is not None:
    print("Connexion réussie")
    connexion.close()
else:
    print("La connexion a échoué")