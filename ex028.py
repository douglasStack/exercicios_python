import random

user=int(input('Qual o número que o computador sorteou de 0 a 5?'))

num=random.randint(1, 5)

print('Você escolheu:', user)
print('Computador sorteou:', num)

if user == num:
    print('VOCE ACERTOUUUU!')
else:
    print('Não foi dessa vez! TENTE NOVAMENTE')