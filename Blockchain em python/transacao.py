import re
import random
import string

class Transacao:
    
    enderecos_gerados = set()
    historico_transacoes = {}

    def __init__(self, remetente, destinatario, valor, transacao_genesis=False):
        if not self.endereco_valido(remetente):
            raise ValueError(f"Endereço de remetente inválido: {remetente}")
        if not self.endereco_valido(destinatario):
            raise ValueError(f"Endereço de destinatário inválido: {destinatario}")
        
        # Permitir valor 0 somente para transação de gênesis
        if valor <= 0 and not transacao_genesis:
            raise ValueError(f"Valor inválido: {valor}. O valor deve ser positivo.")
        
        self.remetente = remetente
        self.destinatario = destinatario
        self.valor = valor

        # Adicionar a transação ao histórico de cada endereço envolvido
        Transacao.adicionar_ao_historico(remetente, self)
        Transacao.adicionar_ao_historico(destinatario, self)

    def __str__(self):
        return f"{self.remetente} envia {self.valor} para {self.destinatario}"

    @staticmethod
    def endereco_valido(endereco):
        # Atualizando o padrão para aceitar qualquer caractere alfanumérico após "2x"
        padrao_endereco = r"^2x[A-Za-z0-9]{48}$"
        return re.match(padrao_endereco, endereco) is not None

    @staticmethod
    def gerar_endereco():
        while True:
            # Gerar 48 caracteres aleatórios
            endereco = "2x" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=48))
            
            # Garantir que o endereço não foi gerado anteriormente
            if endereco not in Transacao.enderecos_gerados:
                Transacao.enderecos_gerados.add(endereco)
                Transacao.historico_transacoes[endereco] = []  # Inicia o histórico para o novo endereço
                return endereco

    @staticmethod
    def adicionar_ao_historico(endereco, transacao):
        # Adiciona a transação ao histórico do endereço, criando o histórico se necessário
        if endereco in Transacao.historico_transacoes:
            Transacao.historico_transacoes[endereco].append(transacao)
        else:
            Transacao.historico_transacoes[endereco] = [transacao]

    @staticmethod
    def mostrar_historico(endereco):
        if endereco in Transacao.historico_transacoes:
            print(f"\n--- Histórico de Transações para o endereço {endereco} ---")
            for transacao in Transacao.historico_transacoes[endereco]:
                print(f"  {transacao}")
            print("-------------------------------")
        else:
            print(f"Nenhuma transação encontrada para o endereço {endereco}.")
