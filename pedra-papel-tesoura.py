import random


print("Escolha: pedra, papel ou tesoura")

entrada = input("Digite sua escolha: ").strip().lower()

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
