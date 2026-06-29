a=float(input('Informe o comprimento:'))
b=float(input('Informe o comprimento:'))
c=float(input('Informe o comprimento:'))

if a + b > c and a + c > b and b + c > a:
    print('\033[0;34m FORMAM UM TRIANGULO \033[m')
else:
    print('\033[0;31m NÃO FORMAM UM TRIANGULO \033[m')