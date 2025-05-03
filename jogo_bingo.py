# gerando uma lista embaralhada de numeros 
from random import shuffle 

TOTAL_NUM = 80

# gerando números aleatórios
def gera_numeros():
  lista_num = list(range(1, TOTAL_NUM-1))
  shuffle(lista_num)
  return lista_num

# gerandoa as cartelas
def gera_cartela():
  lista_num = gera_numeros()
  cartela_num = int(TOTAL_NUM*0.3)
  cartela_set = set(lista_num[:cartela_num])
  return cartela_set

# gerando jogadores
def gera_jogadores(num_jogadores):
  lista_jogadores = []
  
  for cont in range(num_jogadores):
    print('\n\nJogador', cont+1)
    nome = input('Nome do jogador: ')
    cartela = gera_cartela()
    jogador = (nome,cartela)
    lista_jogadores.append(jogador)
  return lista_jogadores

# Durante o jogo, vamos sortear os números e removê-los das cartelas dos jogadores. Assim, o
# jogador que ficar sem números será o vencedor

def remove_numero(lista_jogadores, numero):
  for _, cartela in lista_jogadores:
    if numero in cartela:
      cartela.remove(numero)

# Mostrando os números sorteados
def mostra_jogo(sorteados, lista_jogadores):

  print('*****************************')
  print('* BINGO *')
  print('*****************************')
  print('\nNúmeros sorteados:', sorteados, '\n')

  for jogador in lista_jogadores:
    nome, cartela = jogador
    print(nome, ': ', cartela, sep='')

# Verificando os jogadores vencedores
def busca_vencedores(lista_jogadores):

  vencedores = set()
  
  for nome, cartela in lista_jogadores:
    if len(cartela) == 0:
      vencedores.add(nome)
  return vencedores

# Função principal
def principal():

  print('Iniciando o bingo')
  num_jog = int(input('Informe o número de jogadores: '))
  lista_jogadores = gera_jogadores(num_jog)
  lista_numeros = gera_numeros()
  sorteados = set()

  while True:

    mostra_jogo(sorteados, lista_jogadores)
    print('Pressione ENTER para sortear um número')
    input()
    num = lista_numeros.pop()
    sorteados.add(num)
    remove_numero(lista_jogadores, num)
    vencedores = busca_vencedores(lista_jogadores)

    if len(vencedores) > 0:

      mostra_jogo(sorteados, lista_jogadores)
      print('\nBingo!')
      print('Vencedor(res):', vencedores)

    break

if __name__ == '__main__':
  principal()
