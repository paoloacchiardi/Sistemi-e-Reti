def push(stack,element):
    stack.append(element)
    return stack

def pop(stack):
    element = stack.pop()
    return stack,element

#pila=[1,2,3,"ciao"]
#push(pila,5)
#print(pila)
#pila,element = pop(pila)
#print(pila)
#pila,_=pop(pila) #l'underscore si usa quando non si vuole memorizzare in memoria un valore restituito da una funzione

class carta(object): #creo l'oggetto
    def __init__(self,seme,numero): #self è la classe a cui lui appartiene, questo è il costruttore dell'oggetto
        self.seme = seme
        self.numero = numero

    def stampa(self):
        print(f"La carta ha come seme {self.seme} e come numero {self.numero}.")

c = carta("C", 5)
c.stampa()

Mazzo = []
Semi = ["C","P","D","F"]
for i in range(1,14):
    for s in Semi:
        push(Mazzo,carta(s,i))
for i in Mazzo:
    i.stampa()