import requests 
resposta = requests.get('https://jsonplaceholder.typicode.com/posts/1')

dicionario = resposta.json()

print(dicionario.get("title", "Não existe"))