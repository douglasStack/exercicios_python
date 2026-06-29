#from math import pow
#from math import sqrt

#l_oposto=float(input('Digite o comprimento do lado oposto:'))
#l_adjacente=float(input('Digite o comprimento do lado adjacente:'))

#soma= pow(l_oposto, 2) + pow(l_adjacente, 2)
#hipotenusa = sqrt(soma)
#print('Hipotenusa={}'.format(hipotenusa))

l_oposto=float(input('Digite o comprimento do lado oposto:'))
l_adjacente=float(input('Digite o comprimento do lado adjacente:'))
h=(l_oposto**2 + l_adjacente **2)**(1/2)
print('A hipertenusa vai medir {:.2f}'.format(h))