import random
import time

print("")
print("O JOGO")
print("")
print("pedra, papel e tesoura")
print("")
print("------------------------")
print("")
print("escolha uma opção entre")
print("")
print("-pedra")
print("-papel")
print("-tesoura")
print("")

entrada = input("Digite sua escolha: ").strip().lower()

def jokenpo ():
    time.sleep(1)
    print("JO")
    time.sleep(1)
    print("KEN")
    time.sleep(1)
    print("PO")
    

jokenpo()

print("")

escolhas = ["pedra", "papel", "tesoura"]

if entrada not in escolhas:
   print("Escolha inválida! Tente novamente.")
else:
   computador = random.choice(escolhas)
   print(f"O computador escolheu: {computador}")


if entrada == computador:
    print("Empate!")
    print("")
elif (entrada == "pedra" and computador == "tesoura") or \
        (entrada == "papel" and computador == "pedra") or \
        (entrada == "tesoura" and computador == "papel"):
    print("Você venceu!")
    print("")
else:
    print("Você perdeu!")
    print("")
