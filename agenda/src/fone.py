from src.identificador import Identificador


class Fone:

    def __init__(self, identificador: Identificador, numero: str):
        self.identificador = identificador
        self.numero = numero

    @staticmethod
    def validarNumero(numero: str) -> bool:
        allowed_chars = "0123456789().-"
        for char in numero:
            if char not in allowed_chars:
                return False
        return True

    def getIdentificador(self) -> Identificador:
        return self.identificador

    def getNumero(self) -> str:
        return self.numero
