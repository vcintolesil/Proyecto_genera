import random
def genera(n):
      l = [0] * n
      for i in range(n):
        l[i] = random.randint(0,n)
      return l

a=genera(10)
b=genera(10)
