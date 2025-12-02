from src.pessoa import Pessoa


class Motoca:

    def __init__(self, potencia: int):
        self.potencia = potencia
        self.tempo = 0
        self.pessoa = None

    def getPessoa(self):
        return self.pessoa

    def getTempo(self):
        return self.tempo

    def getPotencia(self):
        return self.potencia

    def subir(self, pessoa: Pessoa):
        if self.pessoa:
            return False
        self.pessoa = pessoa
        return True

    def descer(self):
        if self.pessoa:
            self.pessoa = None
            return True
        return False

    def colocarTempo(self, tempo: int):
        if tempo < 0:
            return False
        self.tempo += tempo
        return True

    def dirigir(self, tempo: int):
        if self.pessoa and self.pessoa.getIdade() <= 10:
            if self.tempo > 0:
                if tempo >= self.tempo:
                    self.tempo = 0
                else:
                    self.tempo -= tempo
                return True
        return False

    def buzinar(self):
        if not self.pessoa:
            return ''
        return 'P' + 'e' * self.potencia + 'm'
