from src.fone import Fone


class Contato:

    def __init__(self, nome):
        self.nome = nome
        self.fones = []

    def getName(self) -> str:
        return self.nome

    def getQuantidadeFones(self) -> int:
        return len(self.fones)

    def getFones(self) -> list:
        return self.fones

    def adicionarFone(self, fone: Fone) -> bool:
        if not Fone.validarNumero(fone.getNumero()):
            return False
        if fone not in self.fones:
            self.fones.append(fone)
            return True
        return False

    def removerFone(self, index: int) -> bool:
        if 0 <= index < len(self.fones):
            self.fones.pop(index)
            return True
        return False
