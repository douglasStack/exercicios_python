sal=float(input('Informe seu salário:'))


if sal > 1.250:
    print('Seu salário com aumento de 10% foi para R$', (sal + (sal * 0.10)))
else:
    print('Seu salário com aumento de 15% foi para R$', (sal + (sal * 0.15)))