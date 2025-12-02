from src.passageiro import Passageiro


class IllegalArgumentException(Exception):
    ...


class Topic:
    def __init__(self, capacidade: int, qtdPrioritarios):
        self.capacidade = capacidade
        if qtdPrioritarios > capacidade:
            raise IllegalArgumentException()

        self.qtdPrioritarios = qtdPrioritarios
        self.assento_normais = capacidade - qtdPrioritarios
        self.PassageiroAssentoNormal = [None] * self.assento_normais
        self.PassageiroAssentoPrioritario = [None] * self.qtdPrioritarios

    def getNumeroAssentosPrioritarios(self):
        return self.qtdPrioritarios

    def getNumeroAssentosNormais(self):
        return self.assento_normais

    def getPassageiroAssentoNormal(self, lugar):
        if lugar < 0 or lugar >= len(self.PassageiroAssentoNormal):
            return None
        return self.PassageiroAssentoNormal[lugar]

    def getPassageiroAssentoPrioritario(self, lugar):
        if lugar < 0 or lugar >= len(self.PassageiroAssentoPrioritario):
            return None
        return self.PassageiroAssentoPrioritario[lugar]

    def getVagas(self):
        return self.PassageiroAssentoPrioritario.count(None) + self.PassageiroAssentoNormal.count(None)

    def subir(self, passageiro: Passageiro):
        if self.getVagas() == 0:
            return False

        if passageiro.ePrioridade():
            if None in self.PassageiroAssentoPrioritario:
                index = self.PassageiroAssentoPrioritario.index(None)
                self.PassageiroAssentoPrioritario[index] = passageiro
                return True
            elif None in self.PassageiroAssentoNormal:
                index = self.PassageiroAssentoNormal.index(None)
                self.PassageiroAssentoNormal[index] = passageiro
                return True
        else:
            if None in self.PassageiroAssentoNormal:
                index = self.PassageiroAssentoNormal.index(None)
                self.PassageiroAssentoNormal[index] = passageiro
                return True
            elif None in self.PassageiroAssentoPrioritario:
                index = self.PassageiroAssentoPrioritario.index(None)
                self.PassageiroAssentoPrioritario[index] = passageiro
                return True
        return False

    def descer(self, nome):
        for i, p in enumerate(self.PassageiroAssentoPrioritario):
            if p is not None and p.getNome() == nome:
                self.PassageiroAssentoPrioritario[i] = None
                return True
        for i, p in enumerate(self.PassageiroAssentoNormal):
            if p is not None and p.getNome() == nome:
                self.PassageiroAssentoNormal[i] = None
                return True
        return False

    def toString(self):
        out = "["
        for p in self.PassageiroAssentoPrioritario:
            out += "@" + (str(p.getNome()) if p is not None else "") + " "
        for p in self.PassageiroAssentoNormal:
            out += "=" + (str(p.getNome()) if p is not None else "") + " "

        return out + "]"
