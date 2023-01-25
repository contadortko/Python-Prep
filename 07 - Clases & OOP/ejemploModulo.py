class Primos:
    def __init__(self):
        self.primoslista = []
    
    def es_primo(self,num):
        if num <= 1:
            return False
        
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    
    def primos_lista(self,num):
        for elemento in range(2,num+1):
            if self.es_primo(elemento):
                self.primoslista.append(elemento)
