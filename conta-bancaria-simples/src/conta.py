class Conta:
    def __init__(self, numero:int, saldo:float):
        self.limite = 100
        self.extrato = []
        self.numero = numero
        self.saldo = saldo + self.limite
        pass

    def getNumero(self):
        return self.numero 

    def getSaldo(self):
        return self.saldo

    def getLimite(self):
        if self.saldo < self.limite:
            return self.saldo
        return self.limite

    def sacar(self, valor: float):
        if valor < 0 or self.saldo - valor < 0:
            return False
        self.saldo -= valor
        self.extrato.append(-float(valor))
        return True

    def depositar(self, valor: float):
        if not valor < 0:
            self.saldo += valor
            self.extrato.append(float(valor))
            return True
        return False

    def transferir(self, destino, valor:float):
        if valor < 0 or self.saldo - valor < 0:
            return False
        self.saldo -= valor
        self.extrato.append(-float(valor))
        destino.depositar(valor)
        return True

    def verExtrato(self):
        return self.extrato
    