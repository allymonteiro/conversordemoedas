# 💱 Conversor de Moedas em Tempo Real

Uma ferramenta de linha de comando feita em Python que busca taxas de câmbio atualizadas e converte valores entre diferentes moedas do mundo.

## ✨ Funcionalidades

- **Interativo e Simples:** Pede ao usuário o valor, a moeda de origem (ex: BRL) e a de destino (ex: USD).
- **Dados em Tempo Real:** Conecta-se à API da ExchangeRate-API para buscar as cotações mais recentes.
- **Resultados Claros:** Exibe a taxa de conversão do dia e o valor final calculado.
- **Tratamento de Erros:** Valida as entradas do usuário e informa caso uma moeda seja inválida ou haja problemas de conexão.
- **Interface Agradável:** Utiliza `colorama` para uma exibição colorida e organizada no terminal.

## ⚙️ Configuração (Para Rodar do Código-Fonte)

1. Clone este repositório.
2. Crie um arquivo chamado `config.py` na raiz do projeto.
3. Dentro do `config.py`, adicione sua chave da ExchangeRate-API:
   ```python
   API_KEY_MOEDAS = "SUA_CHAVE_DA_EXCHANGERATE-API_AQUI"
4. Instale as dependências: pip install -r requirements.txt
5. Execute o script: py conversor.py

## 🚀 Como Usar (Versão Executável para Windows)

1. Vá para a **[Página de Releases](https://github.com/allymonteiro/conversordemoedas/releases)**.
2. Baixe o arquivo `conversor.exe`.
3. Crie o arquivo `config.py` (como ensinado acima) e coloque-o na mesma pasta que o `.exe`.
4. Dê dois cliques para executar!