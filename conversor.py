import requests
import config
from colorama import Fore, Style, init


def converter_moeda():
    API_KEY = config.API_KEYS_MOEDAS
    init(autoreset=True)

    print(Style.BRIGHT + Fore.CYAN + "--- CONVERSOR DE MOEDAS ---")

    try:
        valor = float(
            input("Digite o valor para ser convertido (ex: 99.90): "))
    except ValueError:
        print(Fore.RED + "Valor inválido. Por favor, digite um número.")
        return

    moeda_origem = input(
        "Digite a moeda de origem (ex: BRL, USD, EUR): ").upper().strip()
    moeda_destino = input(
        "Digite a moeda de destino (ex: BRL, USD, EUR): ").upper().strip()
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{moeda_origem}"

    print(Fore.YELLOW +
          f"Buscando taxas de conversão de {moeda_origem} para {moeda_destino}...")

    try:
        response = requests.get(url)
        response.raise_for_status()

        dados = response.json()

        if dados.get('result') == 'success':
            taxas = dados.get('conversion_rates')

            taxa_conversao = taxas.get(moeda_destino)

            if taxa_conversao:
                valor_convertido = valor * taxa_conversao

                print(Style.BRIGHT + Fore.GREEN +
                      "\n--- RESULTADO DA CONVERSÃO ---")
                print(
                    Fore.WHITE + f"  Taxa de conversão: 1 {moeda_origem} = {taxa_conversao} {moeda_destino}")
                print(Style.BRIGHT + Fore.WHITE +
                      f"  Valor convertido: {valor} {moeda_origem} equivale a {valor_convertido:.2f} {moeda_destino}")
                print(Style.BRIGHT + Fore.GREEN +
                      "------------------------------")

            else:
                print(
                    Fore.RED + f"Erro: A moeda destino '{moeda_destino}' não foi encontrada nas taxas de conversão.")
        else:
            erro_api = dados.get('error-type', 'Erro desconhecido na API.')
            print(Fore.RED + f"Erro ao buscar dados da API: {erro_api}")

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(
                Fore.RED + f"Erro: A moeda de origem '{moeda_origem}' é inválida ou não foi encontrada.")
        else:
            print(Fore.RED + f"Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    converter_moeda()
    input("\nPressione Enter para sair.")
