print("------------BOLETIM ESCOLAR-------------")
nome = str(input("Digite seu nome: "))
notapt = float(input("Digite sua notapt: "))
notamt = float(input("Digite sua notamt: "))
notaci = float(input("Digite sua notaci: "))
notaht = float(input("Digite sua notaht: "))

boletim = (notapt + notamt + notaci + notaht) / 4

print("-----------DADOS DO ALUNO--------------")
print(f"Seja bem vindo {nome} :D")
print("")
print(f"BOLETIM: {boletim}")
