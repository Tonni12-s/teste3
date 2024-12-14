class ContaBancaria:
    def __init__(self, saldo, titular):
        self.saldo=saldo
        self.titular= titular


    def depositar (self, valor):
        if valor > 0:
            self.saldo + valor
            print(f"deposito de R${valor} ")


    def sacar (self, valor):
        if valor> 0 :
            self.saldo -=valor
            print (f"saque de R${valor} realizado")



conta = ContaBancaria(1500, 'pedro')


print (conta.saldo, conta.titular)

conta.sacar(500)

print(conta.saldo)

conta.depositar(333)

print(conta.saldo)

