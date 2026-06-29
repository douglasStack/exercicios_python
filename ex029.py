vel=float(input('Qual a velocidade que o carro está andando na avendida:'))
print(vel, 'Km/h')

if vel > 80:
    print('QUE PENA! Voce foi multado!')
    print('O valor da sua multa foi de R$', (vel - 80) * 7)
