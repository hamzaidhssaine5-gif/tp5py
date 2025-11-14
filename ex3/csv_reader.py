import os

class CsvException(Exception):
    pass

class FichierIntrouvableException(CsvException):
    pass

class LigneInvalideException(CsvException):
    pass

class PrixNegatifException(CsvException):
    pass


def charger_csv(chemin):
    if not os.path.exists(chemin):
        raise FichierIntrouvableException("Fichier introuvable.")

    articles = []

    with open(chemin, "r", encoding="utf-8") as f:
        for ligne in f:
            ligne = ligne.strip()
            if not ligne:
                continue

            colonnes = ligne.split(";")
            if len(colonnes) != 3:
                raise LigneInvalideException("Format de ligne invalide.")

            id_, nom, prix_str = colonnes

            try:
                prix = float(prix_str)
            except ValueError:
                raise LigneInvalideException("Le prix doit être un nombre.")

            if prix < 0:
                raise PrixNegatifException("Le prix ne peut pas être négatif.")

            articles.append({"id": id_, "nom": nom, "prix": prix})

    return articles
