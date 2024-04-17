import uuid
from sala import Sala
from professor import Professor

class Disciplina(Sala, Professor):
    diciplinas = {}
    def __init__(self, nome, carga_horaria, horario,numero_Sala , bloco, capacidade, professor):
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.horario = horario
        self.id_Disciplina = uuid.uuid4()
        super().__init__(numero_Sala , bloco, capacidade)
        Disciplina.diciplina[self.id] = self

        if professor is not None:
            if not isinstance(professor, Professor):
                raise TypeError("O professor deve ser uma instância da classe Professor")
            else:
                if Professor.get_Professor(professor.get_Id) is None:
                    raise ValueError("O professor não existe na lista de professores")
                else:
                    self.professor = professor
        else:
            self.professor = None

    @property
    def __get_id__(self):
        return self.id
    
    @classmethod
    def __get_Disciplina(cls, id):
        return cls.diciplina.get(id)
    
    @classmethod
    def __set_Disciplina__(cls, id, nome = None, horario = None, numero_Sala = None, bloco = None, capacidade = None):
        disciplina = cls.__get_Disciplina(id)
        if disciplina:
            if nome:
                disciplina.nome = nome
            if horario:
                disciplina.horario = horario
            if numero_Sala:
                disciplina.numero_Sala = numero_Sala
            if bloco:
                disciplina.bloco = bloco
            if capacidade:
                disciplina.capacidade = capacidade