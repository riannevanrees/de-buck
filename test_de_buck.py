import de_buck
from simple_colors import *

def test_citeer_boek_eerste_druk():
    resultaat = de_buck.citeer_boek(
        auteur="J. Huizinga",
        titel="Herfsttij der Middeleeuwen",
        subtitel="Studie over levens- en gedachtenvormen der veertiende en vijftiende eeuw in Frankrijk en de Nederlanden",
        stad="Haarlem",
        jaar="1919"
        )
    correcte_citatie = "J. Huizinga, "
    correcte_citatie += black("Herfsttij der Middeleeuwen", "italic")
    correcte_citatie += ". "
    subtitel = "Studie over levens- en gedachtenvormen der veertiende en vijftiende eeuw in Frankrijk en de Nederlanden"
    correcte_citatie += black(subtitel, "italic")
    correcte_citatie += " (Haarlem 1919)."
    assert resultaat == correcte_citatie


def test_citeer_boek_latere_druk():
    resultaat = de_buck.citeer_boek(
        auteur="J. Huizinga",
        titel="Herfsttij der Middeleeuwen",
        subtitel="Studie over levens- en gedachtenvormen der veertiende en vijftiende eeuw in Frankrijk en de Nederlanden",
        druk="33",
        stad="Amsterdam",
        jaar="2012"
        )
    correcte_citatie = "J. Huizinga, "
    correcte_citatie += black("Herfsttij der Middeleeuwen", "italic")
    correcte_citatie += ". "
    subtitel = "Studie over levens- en gedachtenvormen der veertiende en vijftiende eeuw in Frankrijk en de Nederlanden"
    correcte_citatie += black(subtitel, "italic")
    correcte_citatie += " (33e druk; Amsterdam 2012)."
    assert resultaat == correcte_citatie


def test_citeer_artikel():
    resultaat = de_buck.citeer_artikel(
        auteur="Elizabeth Edwards",
        titel="Photographic uncertainties",
        subtitel="Between evidence and reassurance",
        tijdschrift="History and Anthropology",
        jaargang=25,
        deel_jaargang=2,
        jaar=2014,
        paginanummers=(171, 188)
        )
    correcte_citatie = "Elizabeth Edwards, "
    correcte_citatie += "'Photographic uncertainties. Between evidence and reassurance', "
    correcte_citatie += black("History and Anthropology", "italic")
    correcte_citatie += " 25:2 (2014) 171-188."
    assert resultaat == correcte_citatie
