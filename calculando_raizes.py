import math

def roots(a,b,c):
  delta = b**2 - 4*a*c
  if a == 0 or delta < 0:
    return()
  elif (delta == 0):
    x1 = b * (-1) / 2 * a
    return (r1,)
  else:
    sqrt_delta = math.sqrt(delta)
    r1 = (b*(-1) + sqrt_delta) / (2*a)  
    r2 = (b*(-1) - sqrt_delta) / (2*a)
    return (r1, r2)

def sec_grade(a,b,c):
  print('Informe os termos da equação Ax² + Bx + C')
  a = float(input('A: '))
  b = float(input('B: '))
  c = float(input('C: '))
  result = roots(a,b,c)
  if len(result) == 0:
    print('\nA equação não é uma equação de segundo grau')
  elif len(result) == 1:
    print('\nA raiz da equação é x =', result[0])
  else: 
    print(f'As raízes dessa função são', end='')
    print('x1 =', result[0], ' e x2 =', result[1])