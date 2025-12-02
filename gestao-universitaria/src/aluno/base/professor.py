from src.aluno.base.funcionario import Funcionario
from src.cliente.tipo import Tipo


class Professor(Funcionario):
    SALARIO_CLASSES = {'A': 3000, 'B': 5000, 'C': 7000, 'D': 9000, 'E': 11000}

    def __init__(self, cpf: str, nome: str, classe: str):
        super().__init__(cpf, nome, Tipo.PROF)
        self._classe = classe

    def getClasse(self) -> str:
        return self._classe

    def getSalario(self) -> float:
        salario_base = self.SALARIO_CLASSES.get(self._classe, 0)
        salario_diarias = self.getDiarias() * 100
        return salario_base + salario_diarias + self.getLucroPessoal()

    def addDiaria(self) -> bool:
        if self.getDiarias() < 3:
            self._diarias += 1
            return True
        return False
