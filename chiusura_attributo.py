import chiave

"Algoritmo della chiusura di un attributo dato uno schema R e un insisme di dipendenze funzionali F definite su R"

# Controlla se un insisme edi attributi sono contenuti in Z
def inclusione(at: list, Z: list) -> bool:
    count = 0
    if type(at) == list:
        for i in at:
            if i in Z: count += 1
    else:
        if at in Z: count += 1
    if count == len(at): return True
    return False

# Controlla quali attributi devono essere inserito in S rispetto Z
def search(F: list[tuple], Z: list, S: list) -> list:
    # Ciclo che esegue il controllo delle dipendenze in F per calcolare la chiusura di Z
    for i in F:
        # Controlla se la parte sinistra della dipendenza i è contenuta in Z e la parte destra non è inclusa in S
        if inclusione(i[0], Z) and not inclusione(i[1], S):
            # Controlla se la parte destra della dipendenza i è un insieme di attributi
            if type(i[1]) == list:
                for at in i[1]: 
                    # Aggiunge gli attribuit delle parti destre delle dipendenze in S una ad una
                    if at not in S: S += at 
            # Se la parte destra non è un insieme ma un singolo attributo aggiunge direttamente l'attributo in S 
            else: S += i[1]
            return S
    # Restituisce S dopo aver aggiunto le parti destre delle dipendenze
    return S

# Unisce due insiemi e li restituisce in un'altra lista
def add_for_list(X: list, S: list) -> list:
    for at in S:
        if at not in X: X += at
    return X

# Main
def main(R: list, F: list[tuple], X: list) -> list:
    Z = X
    S = []
    S = search(F, Z, S)
    # Algoritmo
    while inclusione(S, Z) == False:
        Z = add_for_list(X, S)
        S = search(F, Z, S)
    # Controlla se X è una chiave
    if chiave.check_key(R, F, sorted(Z)) == True and sorted(Z) == R: 
        sub_list = chiave.subset(X, R, F)
        count = 0
        for I in sub_list:
            if chiave.check_key(R, F, I) == True: count += 1
        if count == len(sub_list):
            return sorted(Z)
    # Resituisce Z che è la chiusura di X
    return sorted(Z)