import random
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

print("")

escolhas = ["pedra", "papel", "tesoura"]

if entrada not in escolhas:
    print("Escolha inválida! Tente novamente.")
else:
    
    computador = random.choice(escolhas)
    print(f"O computador escolheu: {computador}")

    
    if entrada == computador:
        print("Empate!")
    elif (entrada == "pedra" and computador == "tesoura") or \
         (entrada == "papel" and computador == "pedra") or \
         (entrada == "tesoura" and computador == "papel"):
        print("Você venceu!")
    else:
        print("Você perdeu!")
