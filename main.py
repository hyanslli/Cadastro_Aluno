import time
import random

class Aluno:
    def __init__(self):
        self.__banco_De_Aluno = {}
    
    def _cadastro(self):
        id = self.gerar_Id()
        atributos = {}
        self.__banco_De_Aluno[id] = atributos

    
    def gerar_Id(self):
        timestamp = int(time.time())
        numero_aleatorio = random.randint(10 ** 1, (10 ** 2) - 1)
        id = (str(timestamp) + str(numero_aleatorio)) 

        while id in self.banco_De_Aluno:
           
            self.gerar_Id()

        return id

