import requests 

resposta = requests.get('https://api.github.com/repos/roberto-silva-dev/cursos-victall')

dicionario = resposta.json()

print("Clone: ",dicionario.get("clone_url", "Não existe"))

print("Description: ",dicionario.get("description", "Não existe"))

print("Language: ",dicionario.get("language", "Não existe"))

print("Defalut Branch: ",dicionario.get("default_branch", "Não existe"))