from src.aluno.base.funcionario import Funcionario
from src.cliente.tipo import Tipo


class Terceirizado(Funcionario):

    def __init__(self, cpf: str, nome: str, insalubre: bool):
        super().__init__(cpf, nome, Tipo.TERC)
        self._insalubre = insalubre

    def getSalario(self) -> float:
        salario_base = 1500.0 if self._insalubre else 1000.0
        return salario_base + self.getLucroPessoal()

    def addDiaria(self) -> bool:
        return False