nb_planches = 10


def calculPluviometrie(quantite_eau, taille_planche, debit, pression):
    print("")
    temps = 0
    return temps


# planche = {"etat": False, "taille": [0, 0], "humidite": [], "temps_arrosage": []}  # dictionnaire

planches = {"0": {"etat": False, "taille": [0, 0], "humidite": [], "temps_arrosage": []}, "1": {"etat": False, "taille": [0, 0], "humidite": [], "temps_arrosage": []}}


def lireCapteursPlanche(numero_planche):
    etat = False
    humidite = 0
    return etat, humidite


def capteursPompe():
    debit = 4  # m3/h
    pression = 4
    return debit, pression


def setTaillePlanche(numero_planche, largeur, longueur):
    print(largeur, longueur)
    planches[str(numero_planche)]["taille"][0] = largeur
    planches[str(numero_planche)]["taille"][1] = longueur
    # print(planches[str(numero_planche)])
    pass


if __name__ == "__main__":
    while 1:
        keys = list(planches.keys())
        print("planches existantes : ", keys)
        res = input("numero_planche ")

        if res in keys:
            print(
                " 1 - set taille \n 2 - set pluviometrie \n 3 - HistoriqueHumidites \n 4 - HistoriqueArossage \n 5 - print planches")
            val = input("valeur : ")
            if (val == "1"):
                largeur = input("largeur : ")
                longueur = input("longueur : ")
                setTaillePlanche(int(res), float(largeur), float(longueur))
            if (val == "5"):
                print(planches)
