import requests


def mensagem_de_abertura():
	print('*-' * 30)
	print(f'{" Consulta de Endereço ":=^60}')
	print('*-' * 30)


def start():
	cep = input('Digite o CEP que você deseja consultar: (Apenas números)\n')

	if len(cep) != 8:
		print('Você não digitou um CEP com o número de digitos corretos, por favor tente novamente')
		start()

	request = requests.get(f'https://viacep.com.br/ws/{cep}/json')

	address = request.json()

	if 'erro' not in address:
		print(request.json())

	else:
		print('CEP inválido')
		while True:
			new_try = int(input('Você deseja realizar uma nova consulta? (1) Para SIM e (2) Para NÃO\n'))

			if new_try == 1:
				start()

			elif new_try == 2:
				exit()


		

invalid_input = True

mensagem_de_abertura()

while invalid_input:
    start()