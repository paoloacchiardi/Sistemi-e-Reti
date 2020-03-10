def readData():
    dict = {}
    vett = []
    data = open('C:/Users/Paolo/Desktop/Tpsit/esercizi/python/grafi/covid_19/data.txt','r')
    lines = data.readlines()
    k = 0
    for line in lines:
        vett[k] = line.split(' ')
        dict[k] = vett[k][1:]
        k+=1
    data.close()
    return dict

def creaMatrixDaDict(dict):
    matrix = []
    for key,val in dict.items():
        matrix[key] = val
    return matrix

def findPatientsZero(mat, righe):
    vect = []
    k = 0
    for k in righe:
        for r in range(0,len(mat)):
            for c in range(0,len(mat[r])):
                if(mat[r][c]==k):
                    vect.append(k)
                    break
            if(mat[r][c]==k):
                break
    return vect

def stampaDict(dict): #stampo un dict
    print("\n{")
    for key, val in dict.items(): #scorro tutto dict
        print(f"\t{key}: {val},") #stampo la key e i val di quella key di dict

    print("}")

def main():
    data = readData()
    stampaDict(data)
    matrix = creaMatrixDaDict(data)
    paziente0 = findPatientsZero(matrix, len(data))
    print(paziente0)

if __name__ == "__main__":
    main()