import random as rand
import re
import string

#filtra strings para melhor uso da library random
def filtro(conteudo=str,letras=False,numeros=False,sinais=False):
    if letras:
        conteudo = re.sub(r"[A-Za-z]"," ",conteudo)
    if numeros:
        conteudo = re.sub(r"[0-9]"," ",conteudo)
    if sinais:
        sinais = [s for s in string.punctuation]
        for s in conteudo:
            if s in sinais:
               conteudo = re.sub(s," ",conteudo)
    return conteudo


class Roll():
    def __init__(self,z=0,x=1,y=20):
        self.x = x
        self.y = y
        self.z = z
    def roll(self):
        if not self.z:
           conteudo = [rand.randint(1,self.y) for x in range(self.x)] 
           return conteudo
        if self.z:
            conteudo = [rand.randint(1,self.y) for x in range(self.x)]
            final = {f"Nº{x+1}":conteudo for x in range (self.z)}
            return final
