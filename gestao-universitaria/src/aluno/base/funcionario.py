from src.cliente.tipo import Tipo


class Funcionario:

    def __init__(self, cpf: str, nome: str, cargo: Tipo):
        self._cpf = cpf
        self._nome = nome
        self._cargo = cargo
        self._diarias = 0
        self._lucro_pessoal = 0.0

    def getNome(self) -> str:
        return self._nome

    def getCpf(self) -> str:
        return self._cpf

    def getCargo(self) -> Tipo:
        return self._cargo

    def getDiarias(self) -> int:
        return self._diarias

    def getLucroPessoal(self) -> float:
        return self._lucro_pessoal

    def addDiaria(self) -> bool:
        return False

    def addLucro(self, valor: float):
        self._lucro_pessoal += valor

    def zerarDiarias(self):
        self._diarias = 0

    def zerarLucro(self):
        self._lucro_pessoal = 0.0

    def getSalario(self) -> float:
        return 0.0

    def __eq__(self, other):
        if isinstance(other, Funcionario):
            return self._cpf == other.getCpf()
        return False