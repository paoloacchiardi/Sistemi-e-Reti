import random as rnd

class  carta(object):
    def __init__(self,seme,numero):
        self.seme = seme
        self.numero = numero
    def stampa(self):
        print(f"la carta ha seme {self.seme} e numero {self.numero}.")

def push(stack,element):
    stack.append(element)
    return stack

def pop(stack):
    element = stack.pop()
    return stack,element

def coppare(mazzo):
    r = rnd.randint(1,52)
    r2 = rnd.randint(1,r)

semi = ["C","Q","P","F"]
mazzo = []
for k in range(0,4):
    for i in range(1,14):
        push(mazzo,carta(semi[k],i))
for k in mazzo:
    k.stampa()

