import networkx as nx
import matplotlib.pyplot as plt

def main():
    v = int(input("Inserire il numero di nodi")) #v è il numero di nodi
    m = creaMatriceDaNumNodi(v) #creo matrice da v nodi
    m = creaMatriceDaDict(d, v) #creo matrice da dict con v nodi
    stampaDict(m) #stampo dict
    stampaMatrice(m, v) #stampo matrice con v nodi


def creaMatriceDaNumNodi(v): #crea una matrice con v nodi
    matrix = [] #inizializzo la matrice
    for i in range(1, v + 1): #ciclo in cui i vale da 1 a numero nodi + 1
        e = [int(i) for i in input(f"Inserire le vicinanze del nodo {i} (usare la '.' come separatore): ").split('.')] #salvo in una lista e tutti i nodi vicino a quello corrente
        colonna = [0 for dim in range(0, v)] #inizializzo la lista colonna a 0
        for j in e: #scorro la lista dei nodi vicini a quelli attuali
            if j != i: #se un elemento della lista e è diverso dal nodo corrente
                colonna[j - 1] = 1 #i nodi vicini ora valgono 1 e non 0 (l'indice di colonna indica il nodo)
        matrix.append(colonna) #aggiungo a matrix la lista colonna

    return matrix


def creaDictDaNumNodi(v): #creo dict con v nodi
    dict = {} #inizializzo dict
    for r in range(0, v): #scorro tutti i nodi
        chiave = r + 1 #chiave vale il nodo corrente + 1
        occ = [int(i) for i in input(f"Inserire le vicinanze del nodo {chiave} (usare la '.' come separatore): ").split('.')] #occ contiene i nodi vicini al nodo numero chiave
        dict[chiave] = occ #la cella numero "chiave" di dict contiene i nodi vicini a quello corrente 

    return dict


def creaDictDaMatrice(grafo):
    dict = {} #inizializzo dict
    for r in range(0, len(grafo)): #scorro tutti i nodi
        chiave = r + 1 #la chiave vale nodo corrente + 1
        occ = [] #inizializzo occ
        for c in range(0, len(grafo)): #secondo for che si esegue n volte dove n è il numero di nodi
            if grafo[r][c] == 1: #se vale 1 vuoldire che il nodo c è vicino al nodo r
                occ.append(c + 1) #aggiungo il nodo vicino a quello corrente ad occ
        dict[chiave] = occ #la cella numero "chiave" di dict assume il valore dei nodi vicini a quello corrente (chiave)

    return dict


def creaMatriceDaDict(dict, v): #creo matrice da dict con v nodi
    matrix = [] #inizializzo la matrice
    for key, val in dict.items(): #key = indice della cella di dict, val = contenuto della cella di dict
        colonna = [0 for dim in range(0, v)] #inizializzo colonna
        for link in val: #scorro i nodi vicini a quello corrente
            colonna[link - 1] = 1 #la cella di colonna che va a valere 1 è la cella che ha come indice il nodo vicino a quello corrente
        matrix.append(colonna) #aggiungo il vettore colonna alla matrice

    return matrix


def stampaMatrice(matrix, v): #stampo una matrice con v nodi
    for r in range(0, v): #scorro tutti i nodi
        print(" ")
        for c in range(0, v): #scorro le vicinanze dei nodi rispetto a quello corrente
            print(matrix[r][c], end=' ') #stampo il collegamento tra il nodo c e r, end fa sì che dopo un print non si vada a capo


def stampaDict(dict): #stampo un dict
    print("\n{")
    for key, val in dict.items(): #scorro tutto dict
        print(f"\t{key}: {val},") #stampo la key e i val di quella key di dict

    print("}")


def drawGrafo(dict): #disegno il grafo di dict tramite networkx
    G = nx.Graph() #creo il grafo
    for key, val in dict.items(): #scorro tutto dict
        G.add_node(key) #aggiungo al grafo la key corrente (nodo)
        for i in val: #scorro tutti i val della key corrente
            G.add_edge(int(key), int(i)) #aggiungo a G i val della key corrente
    print(f"\n{nx.info(G)}") #stampo le info del grafo 
    nx.draw(G)  #disegno il grafo
    plt.show() #mostro il grafo



if __name__ == '__main__': #se questo programma non è importato in un altro programma come una libreria
    main() #eseguo la funzione main