from src.crianca import Crianca


class PulaPula:

    def __init__(self, limiteMax):
        self.LimiteMax = limiteMax
        self.fila = []
        self.CriancasPulando = []
        self.caixa = 0
        self.contas = {}

    def getFilaDeEspera(self):
        return self.fila

    def getCriancasPulando(self):
        return self.CriancasPulando

    def getLimiteMax(self):
        return self.LimiteMax

    def getCaixa(self):
        return self.caixa

    def getConta(self, nome):
        return self.contas.get(nome)

    def entrarNaFila(self, crianca: Crianca):
        for c in self.fila:
            if crianca.getNome() == c.getNome():
                return False
        self.fila.append(crianca)
        return True

    def entrar(self):
        if len(self.CriancasPulando) < self.LimiteMax and self.fila:
            crianca = self.fila.pop(0)
            self.CriancasPulando.append(crianca)
            nome = crianca.getNome()
            self.contas[nome] = self.contas.get(nome, 0) + 2.5
            return True
        return False

    def sair(self):
        if self.CriancasPulando:
            crianca = self.CriancasPulando.pop()
            self.fila.append(crianca)
            return True
        return False
    
    def papaiChegou(self, nome):
        for crianca in list(self.fila):
            if crianca.getNome() == nome:
                self.fila.remove(crianca)
                if nome in self.contas:
                    self.caixa += self.contas.pop(nome)
                return True
        
        for crianca in list(self.CriancasPulando):
            if crianca.getNome() == nome:
                self.CriancasPulando.remove(crianca)
                if nome in self.contas:
                    self.caixa += self.contas.pop(nome)
                return True
                
        return False

    def fechar(self):
        for valor in self.contas.values():
            self.caixa += valor
        
        self.fila.clear()
        self.CriancasPulando.clear()
        self.contas.clear()
        return True