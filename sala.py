import uuid

class Sala:
    salas = {}
    def __init__(self, numero, bloco, capacidade):
        self.numero = numero
        self.bloco = bloco
        self.capaciadde = capacidade
        self.id = uuid.uuid4()

    @property
    def get_id(self):
        return self.id
    
    @classmethod
    def __get_Sala__(cls, id):
        return cls.sala.get(id)
    
    @classmethod
    def __set_Sala__(cls, id, capacidade = None):
        sala = cls.get_Sala(id)
        if sala:
            if capacidade:
                sala.capacidade = capacidade