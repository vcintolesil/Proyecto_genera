print "Hola"
# Maria Fernanda aportando
Def factorial(n):
  f=1
  for in range (1,n+1)
    f*=1
  Return f
# apote patricio ceriche faber, obtener minimo comun multiplo
import math
def mcd(num1, num2):
    a = max(num1, num2)
    b = min(num1, num2)
    while b!=0:
        mcd = b
        b = a%b
        a = mcd
    return mcd

def mcm(n1,n2):
  a = max(n1,n2)
  b = min(n1,n2)
  mcm = ( a / mcd(a,b)) * b
  return mcm
#ecuacion general, Fred Gonzalez
a = float(raw_input('Ingrese a: '))
b = float(raw_input('Ingrese b: '))
c = float(raw_input('Ingrese c: '))

discriminante = b ** 2 - 4 * a * c
if discriminante < 0:
    print 'La ecuacion no tiene soluciones reales'
elif discriminante == 0:
    x = -b / (2 * a)
    print 'La solucion unica es x =', x
else:
    x1 = (-b - (discriminante ** 0.5)) / (2 * a)
    x2 = (-b + (discriminante ** 0.5)) / (2 * a)
    print 'Las dos soluciones reales son:'
    print 'x1 =', x1
    print 'x2 =', x2

raw_input()
