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
    if druk != 1:
        citatie += druk + "e druk; "
    citatie += stad + " " + jaar + ")."
    return citatie


def citeer_artikel(auteur, titel, tijdschrift, jaargang, deel_jaargang, jaar, paginanummers, subtitel="None"):
    citatie = auteur
    citatie += ", "
    citatie += "'"
    citatie += titel
    if subtitel !=  None:
        citatie += ". "
        citatie += subtitel
    citatie += "', "
    citatie += black(tijdschrift, "italic")
    citatie += " {}:{}".format(jaargang, deel_jaargang)
    citatie += " ({}) ".format(jaar)
    citatie += "{}-{}.".format(paginanummers[0], paginanummers[1])
    return citatie


if __name__ == "__main__":
    print("Hi")
    print(red("Test", "italic"))
