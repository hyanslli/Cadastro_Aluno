from disciplina import Disciplina
from professor import Professor
from aluno import Aluno
import uuid

class Curso(Disciplina, Professor, Aluno):
    cursos = {}
    def __init__(self, nome_Curso, carga_Horaria, turno):
        self.nome_Curso = nome_Curso
        self.carga_Horaria = carga_Horaria
        self.id_Curso = uuid.uuid4()
        self.turno = turno
        self.disciplinas = []
        self.professores = []
        self.alunos = []
        Curso.cursos[self.id] = self

    @property
    def get_Id(self): # Retorna o id do curso
        return self.id
    
    @classmethod
    def get_Curso(cls, id): # Retorna o curso pelo id
        return cls.cursos.get(id)