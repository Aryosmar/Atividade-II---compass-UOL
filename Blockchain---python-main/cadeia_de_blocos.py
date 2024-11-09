from bloco import Bloco
from transacao import Transacao

class CadeiaDeBlocos:
    def __init__(self, dificuldade=1):
        self.dificuldade = dificuldade
        self.cadeia = [self.criar_bloco_genesis()]

    def criar_bloco_genesis(self):
        # Criar uma transação de gênesis com endereços válidos de 48 caracteres alfanuméricos
        remetente = Transacao.gerar_endereco()
        destinatario = Transacao.gerar_endereco()
        transacao_genesis = Transacao(remetente, destinatario, 1, transacao_genesis=True)  # Alterado para valor positivo
        return Bloco(0, [transacao_genesis], "0", self.dificuldade)

    def obter_ultimo_bloco(self):
        return self.cadeia[-1]

    def adicionar_bloco(self, novas_transacoes):
        ultimo_bloco = self.obter_ultimo_bloco()
        novo_bloco = Bloco(len(self.cadeia), novas_transacoes, ultimo_bloco.hash_atual, self.dificuldade)
        self.cadeia.append(novo_bloco)

        print(f"\n--- Bloco {novo_bloco.indice} adicionado ---")
        print(f"  Transações:")
        for transacao in novas_transacoes:
            print(f"    {transacao}")
        print(f"  Hash Atual: {novo_bloco.hash_atual}")
        print(f"  Hash Anterior: {novo_bloco.hash_anterior}")
        print(f"  Raiz Merkle: {novo_bloco.arvore_merkle.raiz}")
        print(f"  Nonce: {novo_bloco.nonce}")
        print("---------------------------")

    def validar_integridade(self):
        print("\n--- Validação da Cadeia de Blocos ---")
        for i in range(1, len(self.cadeia)):
            bloco_atual = self.cadeia[i]
            bloco_anterior = self.cadeia[i - 1]

            if bloco_atual.hash_atual != bloco_atual.gerar_hash():
                print(f"  Bloco {bloco_atual.indice} foi alterado!")
                return False

            if bloco_atual.hash_anterior != bloco_anterior.hash_atual:
                print(f"  Bloco {bloco_atual.indice} é inválido!")
                return False

        print("\n--- Cadeia de blocos válida ---")
        return True

    def mostrar_cadeia(self):
        print("\n--- Cadeia de Blocos ---")
        for bloco in self.cadeia:
            print(f"\nBloco {bloco.indice}:")
            print(f"  Transações:")
            for transacao in bloco.transacoes:
                print(f"    {transacao}")  # Exibe a transação de forma detalhada
            print(f"  Hash Atual: {bloco.hash_atual}")
            print(f"  Hash Anterior: {bloco.hash_anterior}")
            print(f"  Raiz Merkle: {bloco.arvore_merkle.raiz}")
            print(f"  Nonce: {bloco.nonce}")
            print("---------------------------")
