from random import randint
numero = int(randint(1, 9))
palpite = 0
tentativa = 0
while palpite != numero:
	palpite = int(input("Seu palpite: "))
	tentativa += 1
	if palpite == numero:
		print("ACERTOU! Placar %i" % tentativa)
	elif palpite < numero:
		print("Chute um valor maior")
	else:
		print("Chute um valor menor")
print ("Fim do Jogo")