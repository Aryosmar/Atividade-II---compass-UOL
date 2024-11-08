from bloco import Bloco
from transacao import Transacao

class CadeiaDeBlocos:
    def __init__(self, dificuldade=1):
        self.dificuldade = dificuldade
        self.cadeia = [self.criar_bloco_genesis()]
        self.historico_transacoes = {}

    def criar_bloco_genesis(self):
        # Criar uma transação de gênesis com endereços válidos de 48 caracteres alfanuméricos
        remetente = Transacao.gerar_endereco()
        destinatario = Transacao.gerar_endereco()
        transacao_genesis = Transacao(remetente, destinatario, 1)  # Alterado para valor positivo
        return Bloco(0, [transacao_genesis], "0", self.dificuldade)

    def obter_ultimo_bloco(self):
        return self.cadeia[-1]

    def adicionar_bloco(self, novas_transacoes):
        ultimo_bloco = self.obter_ultimo_bloco()
        novo_bloco = Bloco(len(self.cadeia), novas_transacoes, ultimo_bloco.hash_atual, self.dificuldade)
        self.cadeia.append(novo_bloco)

        # Adicionar as transações ao histórico de cada endereço
        for transacao in novas_transacoes:
            if transacao.remetente not in self.historico_transacoes:
                self.historico_transacoes[transacao.remetente] = []
            if transacao.destinatario not in self.historico_transacoes:
                self.historico_transacoes[transacao.destinatario] = []

            # Adiciona a transação no histórico de remetente e destinatário
            self.historico_transacoes[transacao.remetente].append(transacao)
            self.historico_transacoes[transacao.destinatario].append(transacao)

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

    def mostrar_historico_transacoes(self, endereco):
        if endereco in self.historico_transacoes:
            print(f"\n--- Histórico de Transações para o endereço {endereco} ---")
            for transacao in self.historico_transacoes[endereco]:
                print(f"  {transacao}")  # Exibe a transação de forma detalhada
            print("-------------------------------")
        else:
            print(f"Nenhuma transação encontrada para o endereço {endereco}.")
