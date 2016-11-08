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

def func(x,array):
  x+=1
  array.append(1)
  return (array)

i=2
array=[1,2]
new_array=func(i,array)
print array
print new_array

for i in new_array:
  print i
  
  
import math 
print "Dame un número"
n= float(input() )
print "su raiz es" (math.sqrt (n))
