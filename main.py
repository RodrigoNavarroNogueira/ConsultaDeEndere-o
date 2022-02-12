import requests

def mensagem_de_abertura():
	print('*-' * 30)
	print(f'{" Consulta de Endereço ":=^60}')
	print('*-' * 30)


def start():
	mensagem_de_abertura()

	cep = input('Digite o CEP que você deseja consultar: (Apenas números)\n')

	if len(cep) != 8:
		print('Você não digitou um CEP com o número de digitos corretos, por favor tente novamente')
		start()

	request = requests.get(f'https://viacep.com.br/ws/{cep}/json')

	print(request.json())

invalid_input = True


while invalid_input:
    start()