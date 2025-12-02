class Tamagotchi:

    def __init__(self, energiaMax:int, saciedadeMax:int, limpezaMax:int, idadeMax:int):
        self.energiaMax = energiaMax
        self.energiaAtual = energiaMax
        self.saciedadeMax = saciedadeMax
        self.saciedadeAtual = saciedadeMax
        self.limpezaMax = limpezaMax
        self.limpezaAtual = limpezaMax
        self.idadeMax = idadeMax
        self.idadeAtual = 0
        self.diamantes = 0
        self.estaVivo = True

    def getEnergiaMax(self):
        return self.energiaMax

    def getSaciedadeMax(self):
        return self.saciedadeMax

    def getLimpezaMax(self):
        return self.limpezaMax

    def getIdadeMax(self):
        return self.idadeMax

    def getEnergiaAtual(self):
        return self.energiaAtual

    def getSaciedadeAtual(self):
        return self.saciedadeAtual

    def getLimpezaAtual(self):
        return self.limpezaAtual

    def getIdadeAtual(self):
        return self.idadeAtual

    def getDiamantes(self):
        return self.diamantes

    def getEstaVivo(self):
        return self.estaVivo

    def _update_stats(self):
        if self.energiaAtual <= 0:
            self.energiaAtual = 0
            self.estaVivo = False
        if self.saciedadeAtual <= 0:
            self.saciedadeAtual = 0
            self.estaVivo = False
        if self.limpezaAtual <= 0:
            self.limpezaAtual = 0
            self.estaVivo = False
        if self.idadeAtual >= self.idadeMax:
            self.idadeAtual = self.idadeMax
            self.estaVivo = False

    def brincar(self):
        if not self.getEstaVivo():
            return False
        self.energiaAtual -= 2
        self.saciedadeAtual -= 1
        self.limpezaAtual -= 3
        self.diamantes += 1
        self.idadeAtual += 1
        self._update_stats()
        return True

    def comer(self):
        if not self.getEstaVivo():
            return False
        self.energiaAtual -= 1
        self.limpezaAtual -= 2
        self.idadeAtual += 1
        self.saciedadeAtual += 4
        if self.saciedadeAtual > self.saciedadeMax:
            self.saciedadeAtual = self.saciedadeMax
        self._update_stats()
        return True

    def dormir(self):
        if not self.getEstaVivo():
            return False
        if self.energiaMax - self.energiaAtual < 5:
            return False
        turnos_dormidos = self.energiaMax - self.energiaAtual
        self.idadeAtual += turnos_dormidos
        self.energiaAtual = self.energiaMax
        self.saciedadeAtual -= 2
        self._update_stats()
        return True

    def banhar(self):
        if not self.getEstaVivo():
            return False
        self.energiaAtual -= 3
        self.saciedadeAtual -= 1
        self.idadeAtual += 2
        self.limpezaAtual = self.limpezaMax
        self._update_stats()
        return True
