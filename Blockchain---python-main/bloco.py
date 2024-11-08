import time
import hashlib
from arvore_merkle import ArvoreMerkle

class Bloco:
    def __init__(self, indice, transacoes, hash_anterior, dificuldade=2):
        self.indice = indice
        self.transacoes = transacoes
        self.timestamp = time.time()
        self.hash_anterior = hash_anterior
        self.nonce = 0
        self.dificuldade = dificuldade
        self.arvore_merkle = ArvoreMerkle(transacoes)
        self.hash_atual = self.proof_of_work()

    def gerar_hash(self):
        dados_bloco = f"{self.indice}{self.timestamp}{self.hash_anterior}{self.arvore_merkle.raiz}{self.nonce}"
        return hashlib.sha256(dados_bloco.encode()).hexdigest()

    def proof_of_work(self):
        hash_desejado = '0' * self.dificuldade
        while not self.gerar_hash().startswith(hash_desejado):
            self.nonce += 1
        return self.gerar_hash()

    def __str__(self):
        return f"Bloco {self.indice}:\nTransações: {', '.join(str(t) for t in self.transacoes)}\nHash Anterior: {self.hash_anterior}\nHash Atual: {self.hash_atual}\nRaiz Merkle: {self.arvore_merkle.raiz}\nNonce: {self.nonce}\n"
