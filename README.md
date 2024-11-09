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
**Navegue até o diretório do projeto:**

cd "Blockchain em python"

### Clone o Repositório
https://github.com/Aryosmar/Atividade-II---compass-UOL.git

## Executando a Aplicação

### No Terminal

1. Navegue até o diretório onde o arquivo `main.py` está localizado.
2. Execute o arquivo `main.py`:
   ```bash
   python main.py

Ou, alternativamente, clique com o botão direito no arquivo `main.py` no Explorer e selecione **Run Python File in Terminal**.

Isso iniciará a aplicação e exibirá a cadeia de blocos atual.

## Detalhes das Classes

### Classe Transacao

**Descrição:** Representa uma transação entre dois endereços, com funcionalidades para gerar endereços válidos e registrar o histórico de transações.

**Atributos:**

- **remetente:** Endereço do remetente.
- **destinatario:** Endereço do destinatário.
- **valor:** Valor da transação.

**Métodos:**

- `__str__()` - Retorna uma representação textual da transação.
- `endereco_valido(endereco)` - Verifica se um endereço está no formato correto.
- `gerar_endereco()` - Gera um endereço único e válido.
- `adicionar_ao_historico(endereco, transacao)` - Adiciona uma transação ao histórico de um endereço.
- `mostrar_historico(endereco)` - Exibe o histórico de transações de um endereço.

### Classe Bloco

**Descrição:** Representa um bloco individual na cadeia de blocos, que contém transações, um hash de bloco anterior, e métodos para realizar o Proof of Work.

**Atributos:**

- **indice:** Índice do bloco na cadeia.
- **transacoes:** Lista de transações do bloco.
- **timestamp:** Timestamp de criação do bloco.
- **hash_anterior:** Hash do bloco anterior.
- **dificuldade:** Nível de dificuldade para o Proof of Work.
- **arvore_merkle:** Raiz de Merkle das transações do bloco.
- **hash_atual:** Hash atual do bloco após o Proof of Work.

**Métodos:**

- `gerar_hash()` - Calcula o hash do bloco com base em seus atributos.
- `proof_of_work()` - Realiza o Proof of Work ajustando o nonce até que o hash satisfaça a dificuldade especificada.
- `__str__()` - Retorna uma representação em string do bloco.

### Classe CadeiaDeBlocos

**Descrição:** Gerencia uma cadeia de blocos, permite adicionar novos blocos e validar a integridade da cadeia.

**Atributos:**

- **dificuldade:** Nível de dificuldade para o Proof of Work em novos blocos.
- **cadeia:** Lista de blocos na cadeia.

**Métodos:**

- `criar_bloco_genesis()` - Cria o bloco gênesis da cadeia.
- `obter_ultimo_bloco()` - Obtém o último bloco da cadeia.
- `adicionar_bloco(novas_transacoes)` - Adiciona um novo bloco à cadeia com as novas transações.
- `validar_integridade()` - Valida a integridade da cadeia de blocos, garantindo a consistência dos hashes.
- `mostrar_cadeia()` - Mostra todos os blocos na cadeia, incluindo transações, hashes e nonce.

### Classe ArvoreMerkle

**Descrição:** A árvore de Merkle permite organizar e validar transações dentro de um bloco de forma eficiente, garantindo a integridade das transações.

**Atributos:**

- **transacoes:** Lista de transações para a construção da árvore.
- **raiz:** Hash raiz da árvore de Merkle, representando todas as transações do bloco.

**Métodos:**

- `construir_arvore(transacoes)` - Constrói a árvore de Merkle, calculando os hashes de cada par de transações até obter o hash da raiz.


```python
import hashlib

def calcular_hash(data): 
    return hashlib.sha256(data.encode()).hexdigest()

class ArvoreMerkle:
    def __init__(self, transacoes):
        self.transacoes = transacoes
        self.raiz = self.construir_arvore(transacoes)

    def construir_arvore(self, transacoes):
        if len(transacoes) == 0:
            return ''
        hashes = [calcular_hash(str(transacao)) for transacao in transacoes]
        while len(hashes) > 1:
            if len(hashes) % 2 != 0:
                hashes.append(hashes[-1])
            hashes = [calcular_hash(hashes[i] + hashes[i + 1]) for i in range(0, len(hashes), 2)]
        return hashes[0]


```

## Funcionalidades

Este projeto permite:

- A criação de uma blockchain com transações entre endereços.
- A adição de blocos à cadeia após passar pelo processo de Proof of Work.
- A validação da integridade da cadeia de blocos.
- A exibição detalhada da cadeia de blocos atual e o histórico de transações para cada endereço.





