#aluno = {
#    "nome" : "Ana",
#    "idade" : "22",
#    "curso" :"Medicina",
#}
#aluno["altura"] = 9.5
#aluno ["curso"] = "Programação"
#print(aluno)
#(aluno.get("compras", "Errado"))

telefone = {
    "luana": "344346-29049",
    "joao": "12859-124785",
    "pedro": "07658-29443"

}
nome = input ("Digite o nome do contato: ")
if nome in telefone:
    print("Telefone", telefone[nome])
else:
    print("Não encontrado")