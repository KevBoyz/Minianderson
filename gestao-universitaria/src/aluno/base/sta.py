from src.aluno.base.funcionario import Funcionario
from src.cliente.tipo import Tipo


class STA(Funcionario):

    def __init__(self, cpf: str, nome: str, nivel: int):
        super().__init__(cpf, nome, Tipo.STA)
        self._nivel = nivel

    def getNivel(self) -> int:
        return self._nivel

    def getSalario(self) -> float:
        salario_base = 1000 + 100 * self._nivel
        salario_diarias = self.getDiarias() * 100
        return salario_base + salario_diarias + self.getLucroPessoal()

    def addDiaria(self) -> bool:
        if self.getDiarias() < 1:
            self._diarias += 1
            return True
        return False
