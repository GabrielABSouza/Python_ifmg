lista_trechos = []
soma_dist = 0
soma_veloc_dist = 0

qtde_trechos = int(input('Informe a quantidade de trechos: '))

for cont in range(qtde_trechos):

  print('\nTrecho', cont+1)
  s = float(input('Distância: '))
  soma_dist += s
  v = float(input('velocidade: '))
  trecho = (s,v)
  lista_trechos.append(trecho)
  soma_veloc_dist += s*v

v_media = soma_veloc_dist/soma_dist
print('A velocidade média foi', v_media)
print('Os trechos com velocidade acima da média foram:')

for cont in range(qtde_trechos):

  s,v = lista_trechos[cont]
  if v > v_media:
    print('Trecho:', cont+1,', distância ',s,',velocidade =', v)