import re
import uuid
from endereco import Endereco

class Professor(Endereco):
    professores = {}
    def __init__(self, nome, cpf, email, rua, bairro, cidade, cep):
        super().__init__(rua, bairro, cidade, cep)
        self.id = uuid.uuid4()
        self.nome = nome
        self.cpf = cpf
        self.email = email
        Professor.professor[self.id] = self

    @staticmethod
    def validar_cpf(cpf): 
        
        if re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
            return cpf
        else:
            raise ValueError(f'CPF inválido: {cpf}')
        
    @staticmethod
    def validar_email(email):
        if re.match(r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]+$', email):
            return email
        else:
            raise ValueError(f'Email inválido: {email}')

    @property
    def get_Id(self): # Retorna o id do professor
        return self.id
    
    @classmethod
    def get_Professor(cls, id): # Retorna o professor pelo id
        return cls.professor.get(id)
    
    @classmethod
    def set_Professor(cls,id, nome = None, cpf = None, email = None, rua = None, bairro = None, cidade = None, cep = None):
        professor = cls.get_Professor(id)
        if professor:
            if nome:
                professor.nome = nome
            if cpf:
                professor.cpf = cpf
            if email:
                professor.email = email
            if rua:
                professor.rua = rua
            if bairro:
                professor.bairro = bairro
            if cidade:
                professor.cidade = cidade
            if cep:
                professor.cep = cep
