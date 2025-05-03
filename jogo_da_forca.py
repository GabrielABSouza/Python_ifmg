# ***JOGO DA FORCA***

#validar se a palavra é válida (não deve conter espaços nem caracteres especiais)
def valida_palavra(palavra):
  for letra in palavra:
    if letra < 'A' or letra > 'Z':
      return False
  return True

# receber a palavra do jogador
def novo_jogo():
  while True:
    print('Informe a palavra para seu adversário')
    print('Não use espaços ou caracteres especiais')
    palavra = input().upper().strip() # strip() remove possíveis espaços em branco no início e final do texto
    if valida_palavra(palavra):
      return palavra
    else:
      print('Palavra inválida! Tente novamente.')

# implementando a lista letras_tela

def tem_letra(palavra, letra, letras_tela):
  encontrada = False
  for cont, carac in enumerate(palavra):
    if carac == letra:
      encontrada = True
      letras_tela[cont] = letra
  return encontrada

# implementando mostra_jogo
# A função join() permite juntar elementos textuais de uma lista usando um delimitador.
# Por exemplo, se temos d=';' e l = ['a', 'b', 'c', 'd'] a instrução d.join(l)
# retorna o texto 'a;b;d;d'

def mostra_jogo(letras_tela, digitadas, erros):
  print('\n'*100)
  print(''.join(letras_tela))
  print('Letras digitadas:', digitadas)
  print('Erros:', erros)

def valida_letra(letra, digitadas):
  if len(letra) != 1:
    return False
  if letra < 'A' or letra > 'Z' or letra in digitadas:
    return False
  return True

# Implementando a função principal
def principal():
  palavra = novo_jogo()
  letras_tela = ['_'] * len(palavra)
  erros = 0
  digitadas = ''

  while True:
    mostra_jogo(letras_tela, digitadas, erros)
    letra = input('Informe uma letra: ').upper().strip()

    if not valida_letra(letra, digitadas):
      continue
    digitadas += letra

    if not tem_letra(palavra, letra, letras_tela):
      erros += 1

      if erros == 5:
        print('Você perdeu!')
        break

    if '_' not in letras_tela:
      print('Você acertou!')
      break

if __name__ == '__main__':
  principal()