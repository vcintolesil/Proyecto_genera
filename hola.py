print "Hola"
#calculadora IVONNE- minimo comun multiplo
 
# Buscar el minimo comun multiplo de dos numeros
 
# define a function
def mcm(x, y):
   """Esta función recibe dos enteros y devuelve el multiplo comum"""
 
   #escoger el mayor de los dos numeros 
   if x > y:
       mayor = x
   else:
       mayor = y
 
   while(True):
       if((mayor % x == 0) and (mayor % y == 0)):
           mcm = mayor
           break
       mayor += 1
 
   return mcm
 
 
# se piden los dos numeros al usuario
num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))
 
print("El minimo comun multiplo de ", num1," y ", num2," es ", lcm(num1, num2))

