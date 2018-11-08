# -*- coding: utf8 -*-
from math import sqrt
# Résolution équation ax2+bx+c=0

print
print 'Résolution d\'une équation du second degré'
print 'Dans R'
print 'de type aX*X + bX + c = 0'
print

#saisie des coef

a=float (input('a = '))
b=float (input('b = '))
c=float (input('c = '))

if b*b-4*a*c < 0 :

	print 'Cette équation n\'a pas de solution réelle'
if b*b-4*a*c == 0  : 
	print 'solution double : x = ', -b/2/a
if b*b-4*a*c > 0 : 
	delta = b*b-4*a*c 
	x1 = (b+sqrt(delta))/2/a
	x2= (b-sqrt(delta))/2/a
	print 'Les solutions sont :'
	print 'x1 = ',x1
	print 'x2 = ',x2
print
#fin 
