nb_planches = 10


def calculPluviometrie(quantite_eau, taille_planche, debit, pression):
    temps = 0
    return temps


planche = {"etat": False, "taille": [0, 0], "humidite": [], "temps_arrosage": []}


def lireCapteursPlanche(numero_planche):
    etat = False
    humidite = 0
    return etat, humidite


def capteursPompe():
    debit = 12
    pression = 4
    return debit, pression


def setTaillePlanche(numero_planche, largeur, longeur):
    pass


if __name__ == "__main__":
    while 1:
        res = input("numero_planche")
        if (res == "1"):
            print("1 - set taille\n2 - set pluviometrie")
            val = input("valeur : ")
            if (val == "1"):
                largeur = input("largeur : ")
                longueur = input("longueur : ")
                setTaillePlanche(int(res), float(largeur), float(longueur))
