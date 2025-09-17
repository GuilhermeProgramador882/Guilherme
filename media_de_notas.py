class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.notas = []

    def apresentar(self):
        return f"{self.nome}, {self.idade} anos, Média: {self.calcular_media()}"

    def adicionar_nota(self, nota):
        self.notas.append(nota)
    
    def calcular_media(self):
        total = sum(self.notas)
        quantidade = len(self.notas)
        return total/quantidade


aluno = Aluno("Gomes", 13)
aluno.adicionar_nota(8.4)
aluno.adicionar_nota(2.9)
aluno.adicionar_nota(3.5)
print(aluno.apresentar())