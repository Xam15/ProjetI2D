nb_planches = 10


def calculPluviometrie(quantite_eau, taille_planche, debit, pression):
    print(quantite_eau, taille_planche)
    taille_planche["largeur * longueur"][0] = planche
    quantite_eau["humidite * taille"][1] = humidite
    quantite_manquante["15 * taille - humidite * taille"][2] = quantite_manquante
    temps = 0
    return temps


# planche = {"etat": False, "taille": [0, 0], "humidite": [], "temps_arrosage": []}  # dictionnaire

planches = {"0": {"etat": False, "taille": [0, 0], "humidite": [], "temps_arrosage": []}, "1": {"etat": False, "taille": [0, 0], "humidite": [], "temps_arrosage": []}}
humidite = {"eau_restant": [0]}
quantite_manquante = {"eau_a_mettre"[0]}


def lireCapteursPlanche(numero_planche):
    etat = False
    capteur.measure()
    humidite = 0
    print("Humidite    : {capteur.humidity():.1}")
    return etat, humidite


def capteursPompe():
    debit = 0.015*["taille"]
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
            if (val == "2"):
                input("lireCapteursPlanche : ")
                planche_taille = input("largeur * longueur : ")
                print(planche_taille)
                humidite = input("humidite * taille : ")
                print(humidite)
                quantite_manquante = input("0.015 * taille - humidite * taille : ")
                print(quantite_manquante)
                calculPluviometrie(int(res), float(planche_taille), float(humidite), float(quantite_manquante))
            if calculPluviometrie < 0.015 :
                capteursPompe = quantite_manquante
                capteursPompe == 1
            else :
                capteursPompe == 0








