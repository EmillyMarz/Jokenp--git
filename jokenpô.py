jog1 = str(input("jog1 escolha uma jogada: "))
jog2 = str(input("jog2 escolha uma jogada: " ))

if jog1 == "papel" and jog2 ==  "pedra" or jog1 == "pedra" and jog2 == "tesoura" or jog1 == "tesoura" and jog2 == "papel":
    print("o jogador 1 ganhou!")

elif jog2 == "papel" and jog1 == "pedra" or jog2 ==  "pedra" and jog1 == "tesoura" or jog2 ==  "tesoura" and jog1 ==  "papel":
   print(" o jogador 2 ganhou! ")

elif jog1 == "papel" and jog2 == "papel" or jog1 == "pedra" and jog2 == "pedra" or jog1 == " tesoura" and  jog2 == "tesoura":
    print("Houve um empate!")

elif  jog1 != "pedra" and jog1 != "papel" and jog1 !=  "tesoura":
    print("Jogador 1 erouuu!")
elif jog2 != "pedra" and jog2 != "papel" and jog2 != "tesoura":
    print("Jogador 2 errouuuuu!")
