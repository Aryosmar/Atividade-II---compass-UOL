from cadeia_de_blocos import CadeiaDeBlocos
from transacao import Transacao

if __name__ == "__main__":
    minha_cadeia = CadeiaDeBlocos(dificuldade=2)

    # Criar algumas transações com endereços válidos de 48 caracteres alfanuméricos
    remetente1 = Transacao.gerar_endereco()
    destinatario1 = Transacao.gerar_endereco()
    transacao1 = Transacao(remetente1, destinatario1, 50)
    
    remetente2 = Transacao.gerar_endereco()
    destinatario2 = Transacao.gerar_endereco()
    transacao2 = Transacao(remetente2, destinatario2, 20)
    
    remetente3 = Transacao.gerar_endereco()
    destinatario3 = Transacao.gerar_endereco()
    transacao3 = Transacao(remetente3, destinatario3, 10)

    # Adicionar blocos com transações
    minha_cadeia.adicionar_bloco([transacao1, transacao2])
    minha_cadeia.adicionar_bloco([transacao3])

    # Mostrar a cadeia de blocos
    minha_cadeia.mostrar_cadeia()

    # Validar a integridade da blockchain
    if minha_cadeia.validar_integridade():
        print("\n--- Cadeia de blocos válida ---")
    else:
        print("\n--- Cadeia de blocos inválida! ---")

    # Mostrar histórico de transações para todos os endereços
    print("\nHistórico de Transações para todos os endereços:")
    for endereco in Transacao.historico_transacoes:
        Transacao.mostrar_historico(endereco)
