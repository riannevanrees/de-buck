from simple_colors import *

def citeer_boek(auteur, titel, stad, jaar, druk=1, locatie="voetnoot", subtitel="None"):
    citatie = auteur
    citatie += ", "
    citatie += black(titel, "italic")
    if subtitel == None:
        citatie += " "
    else:
        citatie += ". " # Nederlandse subtitelstijl
        citatie += black(subtitel, "italic")
        citatie += " "
    citatie += "("
    if druk != 1 and int(druk) <= 10:
        cijfer_naar_telwoord: {2: "tweede", 3: "derde", 4: "vierde", 5: "vijfde",
                               6: "zesde", 7: "zevende", 8: "achtste", 9: "negende",
                               10: "tiende"}
        citatie += cijfer_naar_telwoord[druk] + " druk; "
    elif int(druk) > 10:
        citatie += druk + "e druk; "
    citatie += stad + " " + jaar + ")."
    return citatie


def citeer_artikel(auteur, titel, tijdschrift, jaargang, jaar, paginanummers, subtitel=None, deel_jaargang=None, doi=None, enkele_auteur=True):
    if enkele_auteur:
        citatie = auteur
    else:
        citatie = ", ".join(auteur[0:-1])
        citatie += " en {}".format(auteur[-1])
    citatie += ", "
    citatie += "'"
    citatie += titel
    if subtitel !=  None:
        citatie += ". "
        citatie += subtitel
    citatie += "', "
    citatie += black(tijdschrift, "italic")
    if deel_jaargang == None:
        citatie += " {}".format(jaargang)
    else:
        citatie += " {}:{}".format(jaargang, deel_jaargang)
    citatie += " ({}) ".format(jaar)
    citatie += "{}-{}.".format(paginanummers[0], paginanummers[1])
    if doi != None:
        citatie += " {}.".format(doi)
    return citatie


def citeer_website(website, url, raadpleegdatum):
    # Raadpleegdatum uitgeschreven zoals 23 augustus 2014.
    return website + ", " + url + " (geraadpleegd " + raadpleegdatum + ")."


if __name__ == "__main__":
    citatie1 = citeer_artikel(auteur="J.N. Adams",
                             titel="The Latin of the new Vindolanda tablets",
                             tijdschrift="Britannia",
                             jaargang=50,
                             jaar=2019,
                             paginanummers=(253, 263),
                             doi="https://doi.org/10.1017/S0068113X19000333"
                             )
    print(citatie1)
    citatie2 = citeer_artikel(auteur = ["A.K. Bowdman", "J.D. Thomas", "R.S.O. Tomlin"],
                              titel = "The Vindolanda writing-tablets (Tabulae Vindolandenses IV, part 3)",
                              tijdschrift = "Britannia",
                              jaargang=50,
                              jaar=2019,
                              paginanummers=(225, 251),
                              doi="https://doi.org/10.1017/S0068113X19000321",
                              enkele_auteur=False
                              )
    print(citatie2)
    citatie3 = citeer_website(website="Vindolanda tablets online",
                              url="http://vindolanda.csad.ox.ac.uk",
                              raadpleegdatum="6 december 2023"
                              )
    print(citatie3)
