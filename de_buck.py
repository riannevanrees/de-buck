from simple_colors import *

def citeer_auteur(auteur):
    # Herken of er een of meerdere auteurs zijn en geef de geformatte namen terug.
    # Meerdere auteurs hebben het volgende format: auteur1, auteur2 en auteur3.
    # Er staat geen leesteken of spatie achter.
    if type(auteur) is list:
        citatie = ", ".join(auteur[0:-1])
        citatie += " en {}".format(auteur[-1])
    else:
        citatie = auteur
    return citatie


def citeer_titel(titel, subtitel, italic=True):
    # Geef een schuingedrukte titel terug met een punt tussen de titel en de subtitel.
    # Aanname: de titel en subtitel beginnen met een hoofdletter.
    # Aanname: de hoofdletters in de rest van de zin zijn zoals gewenst.
    # Dan heeft het resultaat de Nederlandse subtitelstijl.
    # Als italic waar is, wordt het schuingedrukt.
    # Anders wordt de titel omringd door aanhalingstekens.
    if subtitel:
        citatie = "{}. {}".format(titel, subtitel)
    else:
        citatie = titel
    if italic:
        return black(citatie, "italic")
    else:
        return "'{}'".format(citatie)


def citeer_publicatie_informatie(druk, stad, jaar):
    # Geef de publicatie-informatie terug, tussen haakjes, in de vorm (druk; stad jaar).
    # Als het de eerste druk is, wordt druk weggelaten.
    # Bij druk 2 tot 10 wordt het telwoord uitgeschreven.
    # Druk moet een int zijn.
    citatie = "("
    if druk != 1 and druk <= 10:
        cijfer_naar_telwoord: {2: "tweede", 3: "derde", 4: "vierde", 5: "vijfde",
                               6: "zesde", 7: "zevende", 8: "achtste", 9: "negende",
                               10: "tiende"}
        citatie += cijfer_naar_telwoord[druk] + " druk; "
    elif druk > 10:
        citatie += "{}e druk; ".format(druk)
    citatie += "{} {})".format(stad, jaar)
    return citatie


def citeer_tijdschrift(tijdschrift, jaargang, deel_jaargang):
    citatie = black(tijdschrift, "italic")
    citatie += " "
    if deel_jaargang == None:
        citatie += "{}".format(jaargang)
    else:
        citatie += "{}:{}".format(jaargang, deel_jaargang)
    return citatie
    

def citeer_boek(auteur, titel, stad, jaar, druk=1, locatie="voetnoot", subtitel=None):
    citatie = citeer_auteur(auteur)
    citatie += ", "
    citatie += citeer_titel(titel, subtitel)
    citatie += " "
    citatie += citeer_publicatie_informatie(int(druk), stad, jaar)
    citatie += "."
    return citatie


def citeer_artikel(auteur, titel, tijdschrift, jaargang, jaar, paginanummers, subtitel=None, deel_jaargang=None, doi=None):
    citatie = citeer_auteur(auteur)
    citatie += ", "
    citatie += citeer_titel(titel, subtitel, italic=False)
    citatie += ", "
    #citatie += black(tijdschrift, "italic")
    #if deel_jaargang == None:
    #    citatie += " {}".format(jaargang)
    #else:
    #    citatie += " {}:{}".format(jaargang, deel_jaargang)
    #citatie += " ({}) ".format(jaar)
    citatie += citeer_tijdschrift(tijdschrift, jaargang, deel_jaargang)
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
    #print(citatie1)
    citatie2 = citeer_artikel(auteur = ["A.K. Bowdman", "J.D. Thomas", "R.S.O. Tomlin"],
                              titel = "The Vindolanda writing-tablets (Tabulae Vindolandenses IV, part 3)",
                              tijdschrift = "Britannia",
                              jaargang=50,
                              jaar=2019,
                              paginanummers=(225, 251),
                              doi="https://doi.org/10.1017/S0068113X19000321",
                              )
    #print(citatie2)
    citatie3 = citeer_website(website="Vindolanda tablets online",
                              url="http://vindolanda.csad.ox.ac.uk",
                              raadpleegdatum="6 december 2023"
                              )
    #print(citatie3)
    citatie4 = citeer_website(website = "Brill's new Pauly: Polybius",
                              url = "http://dx.doi.org.ru.idm.oclc.org/10.1163/1574-9347_bnp_e1000940",
                              raadpleegdatum = "9 december 2023"
                              )
    print(citatie4)
    citatie5 = citeer_boek(auteur = "Arthur M. Eckstein",
                           titel = "Moral vision in the histories of Polybius",
                           stad = "Berkeley",
                           jaar = "1995")
    print(citatie5)
    citatie6 = citeer_artikel(auteur = ["David Ingles", "Roland Robertson"],
                              titel = "From republican virtue to global imaginary",
                              subtitel = "Changing visions of the historian Polybius",
                              tijdschrift = "History of the human sciences",
                              jaargang = 19,
                              deel_jaargang = 1,
                              jaar = 2006,
                              paginanummers = (1, 18),
                              doi = "https://doi-org.ru.idm.oclc.org/10.1177/0952695106062144"
                              )
    print(citatie6)
