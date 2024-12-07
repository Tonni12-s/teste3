class Carro:
    def __init__(self, cor, modelo, ano, marca):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.marca = marca
        self.capacidade = 50
        self.tanque = 0
        self.ligado = False

    def ligar(self):
        self.ligado = True

    def abastecer(self, qtd):
        if(self.tanque + qtd <= self.capacidade):
            self.tanque += qtd
        else:
            print("Não foi possível abastecer")


meu_carro = Carro("preto", "supra", 2019, "Toyota")

print(meu_carro.tanque)
meu_carro.abastecer(20)
print(meu_carro.tanque)
meu_carro.abastecer(25)
print(meu_carro.tanque)


