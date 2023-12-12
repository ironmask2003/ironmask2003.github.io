import chiusura_attributo
import chiave

"Main per inserire lo schema relazionale R e l'insieme di dipende funzionali F definite su R"

# Inserimento dello schema R
def insert_R():
    temp = input("Inserisci lo schema Relazionale R con gli attributi separati da una virgola senza spazio: ")
    return temp.split(",")

# Inserimento dell'insisme delle dipendenze definite su R
def insert_F():
    finish = False
    F = []
    # Ciclo che permette di inserire delle dipendenze in F fino a quando l'utente non inserisce 1 o 0
    while finish != True:
        det_1 = input("Inserisci la parte sinistra della dipendenza: ")
        if det_1 == "1" or det_1 == "0": break
        det_2 = input("Inserisci la parte destra della dipendenza: ")
        if det_2 == "1" or det_2 == "0": break
        # Controlla se i dati inseriti sono insiemi di attribuiti o singoli attributi
        if len(det_1) == 1 and len(det_2) == 1: F.append((det_1, det_2))    # Parte sinistra e destra sono singoli attributi
        elif len(det_1) == 1: F.append((det_1, det_2.split(",")))           # Parte sinistra è un singolo attributo
        elif len(det_2) == 1: F.append((det_1.split(","), det_2))           # Parte destra è un singolo attributo
        else: F.append((det_1.split(","), det_2.split(",")))                # Parte sinistra e destra sono insiemi di attributi
    return F

# Calcolo della chiavi di uno schema
def cal_keys(R: list, F: list):
    check_keys = chiave.check_keys(R, F)
    for K in check_keys:
        print(chiusura_attributo.main(R, F, K))
    return

# Calcolo della chiusura di un attributo
def calc_closure(R: list, F: list):
    at = input("Inserisci l'attributo: ")
    at = at.split(",")
    closure = chiusura_attributo.main(R, F, at)
    print(closure)
    return

# main
def main():
    # Inserimento dello schema R
    R = insert_R()
    # Inserimento dell'insieme delle dipendenze F su R
    F = insert_F()
    # Richieste dell'utente
    opt = input("""Cosa fare:
1. Calcolare la chiusura di un attributo
2. Calcolare tutte le chiavi di uno Schema \n""")
    if opt == "1": calc_closure(R, F)
    elif opt == "2": cal_keys(R, F)
    return


# Funzioni di Test
def prova(R: list, F: list, X: list[list]) -> list:
    result_X = []
    for at in X:
        result_X.append(calc_closure_prova(R, F, at))
    keys = cal_keys_prova(R, F)
    return result_X, keys

def calc_closure_prova(R: list, F: list, K: list) -> list:
    closure = chiusura_attributo.main(R, F, K)
    return closure

def cal_keys_prova(R: list, F: list) -> list:
    check_keys = chiave.check_keys(R, F)
    result = []
    for K in check_keys:
        if chiave.check_key(R, F, K): result.append(K)
    return result