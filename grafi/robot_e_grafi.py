#Acchiardi Paolo - es. Robot e grafi

from sys import exit

def main():
    matrice = []
    dim = int(input("Inserisci il numero di righe della matrice quadrata:\t"))
    if(dim<=0):
        exit("Errore")
    matrice = [ [ 0 for i in range(dim) ] for j in range(dim) ] #inizializzo a 0 le celle della matrice
    while True:
        risp = input("Vuoi inserire un nodo? \"si\" o \"no\":\t")
        if(risp == "si"):
            riga = int(input("Inserisci la riga:\t"))
            colonna = int(input("Inserisci la colonna:\t"))
            if(riga<0 or colonna<0 or riga>=dim or colonna>=dim):
                break
            matrice[riga][colonna] = True
        else:
            break
    matrice_to_dict(matrice, dim, dim)
    
    
def matrice_to_dict(matrice, righe, colonne):
    matrice2 = [ [ None for i in range(righe) ] for j in range(colonne) ]
    k=0
    for counter in range(0,righe):
        for countertwo in range(0,colonne):
            if(matrice[counter][countertwo]):
                matrice2[counter][countertwo] = k
                k+=1
    dict = {}
    for counter in range(0,righe):
        for countertwo in range(0,colonne):
            vett = []
            if(matrice2[counter][countertwo] != None): #counter = righe, countertwo = colonne
                key = matrice2[counter][countertwo]
                if(counter!=0 and countertwo!=0): #inizio controlli che verificano dove si trova la cella e quante celle adiacenti ha (il contenuto non importa)
                    if(matrice2[counter-1][countertwo-1] != None):
                        vett.append(matrice2[counter-1][countertwo-1])
                if(counter!=0):
                    if(matrice2[counter-1][countertwo]!=None):
                        vett.append(matrice2[counter-1][countertwo])
                    if(matrice2[counter][countertwo-1]):
                        vett.append(matrice2[counter][countertwo-1])
                if(counter!=0 and countertwo!=colonne-1): 
                    if(matrice2[counter-1][countertwo+1] != None):
                        vett.append(matrice2[counter-1][countertwo+1])
                if(countertwo!=colonne-1):
                    if(matrice2[counter][countertwo+1] != None):
                        vett.append(matrice2[counter][countertwo+1])
                if(counter!=righe-1 and countertwo!=0):
                    if(matrice2[counter+1][countertwo-1] != None):
                        vett.append(matrice2[counter+1][countertwo-1])
                if(counter!=righe-1):
                    if(matrice2[counter+1][countertwo] != None):
                        vett.append(matrice2[counter+1][countertwo])
                if(counter!=righe-1 and countertwo!=colonne-1):
                    if(matrice2[counter+1][countertwo+1] != None):
                        vett.append(matrice2[counter+1][countertwo+1])
                dict[key] = vett
    stampaDict(dict)


def stampaDict(dict): #stampo un dict
    print("\n{")
    for key, val in dict.items(): #scorro tutto dict
        print(f"\t{key}: {val},") #stampo la key e i val di quella key di dict

    print("}")


if __name__ == "__main__":
    main()