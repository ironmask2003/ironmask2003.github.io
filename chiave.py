"Algoritmo che controlla se l'insieme di attributi trovato con l'algoritmo del calcolo della chiusura è una chiave"

# Funzione che aggiugne gli elementi della parte destra della dipendenza presa in input alla lista presa in input controllando se gli attributi sono già presenti o no
def add_elem(dip: list, temp: list) -> list:
    for i in dip[1]: 
        # Se l'attributo non è presente lo aggiunge
        if i not in temp: temp.append(i)
    return temp

# Calcola i sottoinsismi di un insisme di attributi che potrebbero essere chiavi
def subset(K: list, R: list, F: list):
    # Attributi che devono essere presenti nelle chiavi
    imp_at = check_dipendenze(R, F)
    # Lista contente tutti i sottoinsismi di K da cui controllare se anche loro sono chiavi
    sub_list = []
    # Indice per tenere la posizione degli attributi presenti in K che sono anche in imp_at
    idx = 0
    # Ciclo che crea i sottoinsiemi di K
    for at in K:
        # Se in K è presente un attributo in imp_at, allora passa al ciclo successivo
        if at in imp_at: idx = K.index(at); continue
        if idx != 0: sub_list.append([at, K[idx]])
        else: sub_list.append([at])
    # Se K ha dei sottoinsiemi aggiunge ad ogni sottoinsieme gli attributi di imp_at
    if sub_list != []:
        # Ciclo che itera sui sottoinsimi di k
        for at in sub_list:
            # Ciclo che itera su imp_at e controlla se gli elementi sono presenti nei sottoinsiemi di K
            for elem in imp_at:
                if elem not in at: at.append(elem)
    return sub_list

# Controlla quali attributi devono essere presenti nelle chiavi
def check_dipendenze(R: list, F: list) -> list:
    temp = []
    for dip in F:
        temp = add_elem(dip, temp)
    final = []
    for at in R:
        if at not in temp: final.append(at)
    return final

# Controlla se la chiave K presa in input è valida ed ha gli attributi fondamentali per essere una chiave
def check_key(R: list, F: list, K: list) -> bool:
    # Attributi che non sono presenti nella parti sinistre delle dipendenze in F
    important_at = check_dipendenze(R, F)
    # Controlla se gli sttributi della lista important_at sono presenti nella chiave K in input
    count = 0
    for at in K:
        if at in important_at: count += 1
    if count ==  len(important_at): return True
    return False

# Funzione che controlla se gli elementi in at sono inclusi in Z
def inclusione(at: list, Z: list) -> bool:
    count = 0
    for i in at:
        if i in Z: count += 1
    if count == len(at): return True
    return False

# Controlla quali sono le possibili chiavi
def check_keys(R: list, F: list):
    # Lista delle chiavi 
    key_chek = []
    # Attributi che non sono presenti nella parte destra delle dipendenze di F
    un_used_at = (check_dipendenze(R, F))
    # Lista degli elementi da eliminare
    pos = []
    # Ciclo for che aggiunge nella lista delle chiavi possibli le parti destre di ogni dipendenza in F
    for dip in F:
        if dip[0] not in key_chek: key_chek.append(dip[0])
    # Ciclo che aggiunge alle possibili chiavi gli attributi che non appaiono nella parti destre di ogni dipendenza in F
    for I in key_chek:
        # Controlla se l'attributo è un'insisme di attributi
        if type(I) == list : 
            # Ciclo che aggiuge gli attributi mancanti per far diventare la chiave valida
            for at in un_used_at:
                if at not in I: I += at
            I.sort()
            # Controlla se esiste un elemento presente in key_chek che è un suo sottoinsieme, se lo è elimina l'elemento I
            for ins in key_chek:
                if inclusione(ins, I) and (key_chek.index(ins) != key_chek.index(I)): pos.append(key_chek.index(I))
        # Altrimenti l'attributo non è un insisme e lo rende una lista e aggiugne gli elementi mancanti all'insieme
        else: 
            idx = key_chek.index(I)
            I = list(I)
            # Ciclo che aggiunge gli attrbiuti mancanti
            for at in un_used_at:
                if at not in I: I += at
            I.sort()
            for ins in key_chek:
                if inclusione(ins, I) and (key_chek.index(ins) != idx): pos.append(idx)
    # Controlla se ci sono elementi da eliminare perchè già presenti
    count = 0
    for ind in pos:
        try: key_chek.remove(key_chek[ind]); count += 1
        except IndexError: key_chek.remove(key_chek[ind - count])
    # Resituisce la lista delle possibili chiavi
    return key_chek