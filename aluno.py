import re
import uuid
from endereco import Endereco

class Aluno(Endereco):
    alunos = {}
    def __init__(self, nome, cpf, email, rua, bairro, cidade, cep):
        super().__init__(rua, bairro, cidade, cep)
        self.id = uuid.uuid4()
        self.nome = nome
        self.cpf = cpf
        self.email = email
        Aluno.aluno[self.id] = self

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
    def get_Id(self): # Retorna o id do aluno
        return self.id
    
    @classmethod
    def get_Aluno(cls, id): # Retorna o aluno pelo id
        return cls.aluno.get(id)
    
    @classmethod
    def set_Aluno(cls,id, nome = None, cpf = None, email= None, rua = None, bairro = None, cidade = None, cep = None):
        aluno = cls.get_Aluno(id)
        if aluno:
            if nome:
                aluno.nome = nome
            if cpf:
                aluno.cpf = cpf
            if email:
                aluno.email = email
            if rua:
                aluno.rua = rua
            if bairro:
                aluno.bairro = bairro
            if cidade:
                aluno.cidade = cidade
            if cep:
                aluno.cep = cep