import re
class Endereco:
    enderecos = {}
    def __init__(self, rua, bairro, cidade, cep):
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep
        Endereco.enderecos[self.cep] = self

    @staticmethod
    def validar_cep(cep):
        if re.match(r'\d{5}-\d{3}', cep):
            return cep
        else:
            raise ValueError(f'CEP inválido: {cep}') 
        
    @property
    def get_Cep(self):
        return self.cep
    
    @classmethod
    def get_Endereco(cls, cep):
        return cls.enderecos.get(cep)
    
    @classmethod
    def set_Endereco(cls, cep, rua = None, bairro = None, cidade = None):
        endereco = cls.get_Endereco(cep)
        if endereco:
            if rua:
                endereco.rua = rua
            if bairro:
                endereco.bairro = bairro
            if cidade:
                endereco.cidade = cidade
            if cep:
                endereco.cep = cep 