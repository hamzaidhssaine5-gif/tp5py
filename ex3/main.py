from csv_reader import (
    charger_csv,
    FichierIntrouvableException,
    LigneInvalideException,
    PrixNegatifException,
)

def main():
    chemin = "articles.csv"

    try:
        articles = charger_csv(chemin)
        print("Articles chargés :")
        for art in articles:
            print(art)

    except FichierIntrouvableException as e:
        print("Erreur :", e)
    except LigneInvalideException as e:
        print("Erreur dans une ligne du CSV :", e)
    except PrixNegatifException as e:
        print("Erreur prix :", e)


if __name__ == "__main__":
    main()
