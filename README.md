# Sistema de Transações em Blockchain

Sistema de transações em uma blockchain com estrutura de classes para criar, validar e armazenar transações em blocos. Este projeto faz parte do desafio na trilha de aprendizado do programa de bolsas de Blockchain da Compass UOL.

## Pré-Requisitos

Antes de executar a aplicação, você precisará dos seguintes pré-requisitos:

- Python 3.6 ou superior
- Bibliotecas `hashlib`, `time`, `re`, `random`, e `string` (todas incluídas no Python padrão)

## Estrutura do Projeto

O projeto é estruturado em cinco arquivos principais:

1. **transacao.py:** Define a classe `Transacao`, que representa uma transação entre usuários e gerencia o histórico de transações para cada endereço.
2. **bloco.py:** Define a classe `Bloco`, que representa um bloco na cadeia de blocos, incluindo a lógica para calcular seu hash e realizar o Proof of Work.
3. **cadeia_de_blocos.py:** Define a classe `CadeiaDeBlocos`, que gerencia a coleção de blocos, implementa a lógica para adicionar novos blocos e validar a integridade da cadeia.
4. **arvore_merkle.py:** Define a classe `ArvoreMerkle`, que organiza e valida transações dentro de um bloco através de uma árvore de Merkle.
5. **main.py:** Arquivo de execução principal que cria transações e blocos e adiciona-os à cadeia, além de exibir o histórico de transações e validar a integridade da cadeia de blocos.

## Configuração Inicial

### Clone o Repositório
https://github.com/Aryosmar/Atividade-II---compass-UOL.git
''


