from src.aluno.base.funcionario import Funcionario
from src.aluno.base.professor import Professor
from src.aluno.base.sta import STA
from src.cliente.irh_service import IRHService
from src.cliente.tipo import Tipo


class RHService(IRHService):

    def __init__(self):
        self._funcionarios = {}

    def cadastrar(self, funcionario: Funcionario) -> bool:
        if funcionario.getCpf() in self._funcionarios:
            return False

        if isinstance(funcionario, Professor):
            if funcionario.getClasse() not in Professor.SALARIO_CLASSES:
                return False
        elif isinstance(funcionario, STA):
            if not 1 <= funcionario.getNivel() <= 30:
                return False

        self._funcionarios[funcionario.getCpf()] = funcionario
        return True

    def remover(self, cpf: str) -> bool:
        if cpf in self._funcionarios:
            del self._funcionarios[cpf]
            return True
        return False

    def obterFuncionario(self, cpf: str) -> Funcionario:
        return self._funcionarios.get(cpf)

    def getFuncionarios(self) -> list:
        return sorted(list(self._funcionarios.values()), key=lambda f: f.getNome())

    def getFuncionariosPorCategorias(self, tipo: Tipo) -> list:
        lista = [f for f in self._funcionarios.values() if f.getCargo() == tipo]
        return sorted(lista, key=lambda f: f.getNome())

    def getTotalFuncionarios(self) -> int:
        return len(self._funcionarios)

    def solicitarDiaria(self, cpf: str) -> bool:
        func = self.obterFuncionario(cpf)
        if func:
            return func.addDiaria()
        return False

    def partilharLucros(self, valor: float) -> bool:
        if not self._funcionarios:
            return False
        lucro_individual = valor / len(self._funcionarios)
        for func in self._funcionarios.values():
            func.addLucro(lucro_individual)
        return True

    def iniciarMes(self):
        for func in self._funcionarios.values():
            func.zerarDiarias()
            func.zerarLucro()

    def calcularSalarioDoFuncionario(self, cpf: str) -> float:
        func = self.obterFuncionario(cpf)
        if func:
            return func.getSalario()
        return None

    def calcularFolhaDePagamento(self) -> float:
        return sum(func.getSalario() for func in self._funcionarios.values())