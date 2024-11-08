import hashlib

# Função para calcular o hash de um dado
def calcular_hash(dado):
    return hashlib.sha256(dado.encode('utf-8')).hexdigest()

class ArvoreMerkle:
    def __init__(self, transacoes):
        self.transacoes = transacoes
        self.raiz = self.construir_arvore(transacoes)

    def construir_arvore(self, transacoes):
        if len(transacoes) == 0:
            return None
        if len(transacoes) == 1:
            return calcular_hash(str(transacoes[0]))

        # Calcular o hash das transações
        hashes = [calcular_hash(str(transacao)) for transacao in transacoes]

        # Construir a árvore de Merkle
        while len(hashes) > 1:
            if len(hashes) % 2 != 0:
                hashes.append(hashes[-1])  # Duplicar o último hash se o número for ímpar

            hashes = [calcular_hash(hashes[i] + hashes[i + 1]) for i in range(0, len(hashes), 2)]

        return hashes[0]

    def verificar_enderecos(self):
        for transacao in self.transacoes:
            if not self.endereco_valido(transacao.remetente) or not self.endereco_valido(transacao.destinatario):
                return False
        return True

    def endereco_valido(self, endereco):
        # Verificar se o endereço possui a estrutura desejada (ex: 50 caracteres hexadecimais)
        return len(endereco) == 50 and endereco[:2] == "2x" and all(c in "0123456789abcdef" for c in endereco[2:])
