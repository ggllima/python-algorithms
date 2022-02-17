from copy import deepcopy
class Pilha():
    def __init__(self, lista):
        self.lista = lista
        
    def empty(self):
        if not self.lista:
            return True
        return False
        
    def push(self, element):
        if self.empty() == True:
            self.lista.append(element)
            return self.lista
        else:
            self.lista.append(element)
            index = 1
            ultimo = self.lista[-1]
            while index <len(self.lista):
                self.lista[-index] = self.lista[-index-1]
                index+=1
            self.lista[0] = ultimo
            return self.lista
        
    def pop(self):
        if self.empty() == True:
            print("Empty list")
        else:
            nova_lista = []
            index = 1
            primeira = self.lista[0]
            while index < len(self.lista):
                nova_lista.append(self.lista[index])
                index+=1
            self.lista = deepcopy(nova_lista)
            return primeira
    
    def top(self):
        if self.empty() == True:
            print("Empty list")
        else:
            return self.lista[len(self.lista)-1]
        