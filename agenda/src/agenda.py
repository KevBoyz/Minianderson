from src.contato import Contato
from src.identificador import Identificador


class Agenda:

    def __init__(self):
        self.contatos = []

    def getContatos(self) -> list:
        return self.contatos

    def getQuantidadeDeContatos(self) -> int:
        return len(self.contatos)

    def getContato(self, nome: str) -> Contato:
        if self.contatos:
            for c in self.contatos:
                if c.getName() == nome:
                    return c
        return None

    def adicionarContato(self, contato: Contato) -> bool:
        if contato.getQuantidadeFones() == 0:
            return False
        existing_contact = self.getContato(contato.getName())
        if existing_contact:
            for fone in contato.getFones():
                existing_contact.adicionarFone(fone)
            return False

        self.contatos.append(contato)
        self.contatos.sort(key=lambda c: c.getName())
        return True

    def removerContato(self, nome: str) -> bool:
        contato = self.getContato(nome)
        if contato:
            self.contatos.remove(contato)
            return True
        return False

    def removerFone(self, nome: str, index: int) -> bool:
        contato = self.getContato(nome)
        if contato:
            return contato.removerFone(index)
        return False

    def getQuantidadeDeFonesPorIdentificador(self, identificador: Identificador) -> int:
        count = 0
        for contato in self.contatos:
            for fone in contato.getFones():
                if fone.getIdentificador() == identificador:
                    count += 1
        return count

    def getQuantidadeTotalDeFones(self) -> int:
        count = 0
        for contato in self.contatos:
            count += contato.getQuantidadeFones()
        return count

    def pesquisar(self, expressao: str) -> list:
        resultado = []
        for contato in self.contatos:ç
            if expressao in contato.getName():
                if contato not in resultado:
                    resultado.append(contato)
            for fone in contato.getFones():
                if expressao in fone.getNumero():
                    if contato not in resultado:
                        resultado.append(contato)
                if expressao in fone.getIdentificador().value:
                    if contato not in resultado:
                        resultado.append(contato)
        return resultado