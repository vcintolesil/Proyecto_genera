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
