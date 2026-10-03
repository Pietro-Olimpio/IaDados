import requests

cep = input("Digite seu cep: ")


url = f"https://viacep.com.br/ws/{cep}/json/"

resposta = requests.get(url)
dados = resposta.json()

print(f"Tu mora na rua {dados["logradouro"]}, no bairro  {dados["bairro"]} na cidade de {dados["localidade"]}")