# Caixa de supermercado

DESCRICAO = 'DESCRIÇÃO'
ESTOQUE = 'ESTOQUE'
PRECO = 'PREÇO'

# Cadastro de produtos
def cad_produto(dic_produtos):

  print('Cadastrar/atualizar produto')
  codigo = int(input('Código do produto: '))

# Caso o produto já esteja cadastrado
  if codigo in dic_produtos:
    produto = dic_produtos[codigo]
    print('\nProduto existente:\n', produto)

# Caso o produto não esteja cadastrado
  else:
    print('\nProduto não encontrado')
    descricao = input('Informe a descrição: ')
    produto = {DESCRICAO: descricao}
    dic_produtos[codigo] = produto

  produto[ESTOQUE] = float(input('Estoque: '))
  produto[PRECO] = float(input('Preço: '))


# Listando os produtos na tela do usuário
def listar_produtos(dic_produtos):

  if len(dic_produtos) == 0:
    print('\nnenhum produto encontrado!')
    return
  
  for codigo, produto in dic_produtos.items():
    print('CÓDIGO:', codigo, produto)

  input('Pressione ENTER para voltar')

# Realizando a venda

def venda(dic_produtos, lista_vendas):

  print('\nVenda de produto')
  codigo = int(input('Código do produto: '))

  if codigo not in dic_produtos:
    print('Produto não encontrado!')
    return

  produto = dic_produtos[codigo]
  print('\nProduto:\n',produto)
  quant = float(input('Quantidade vendida: '))

  if quant > produto[ESTOQUE]:
    print('\nEstoque insuficiente!')
    return

  print('Total da venda:', produto[PRECO]*quant)
  venda = (codigo, quant, produto[PRECO])
  produto[ESTOQUE] -= quant
  lista_vendas.append(venda)

# Gerando relatório de vendas

def relatorio_vendas(dic_produtos, lista_vendas):

  if len(lista_vendas) == 0:
    print('Nenhuma venda encontrada!')
    return
  total_geral = 0

  for codigo, quant, preco in lista_vendas:
    produto = dic_produtos[codigo]
    print('CÓDIGO:', codigo, end=' ')
    print('| PRODUTO:', produto[DESCRICAO], end=' ')
    print('| QUANTIDADE:', quant, end=' ')
    print('| PREÇO:', preco, end=' ')
    total = quant * preco
    print('| TOTAL:', total)
    total_geral += total

  print('TOTAL GERAL:', total_geral)
  input('Pressine ENTER para voltar')


# Gerando menu de navegação

def menu():

  print('\n*****************************')
  print('* CAIXA *')
  print('*****************************')
  print('(C)adastrar/atualizar produto')
  print('(L)istar produtos ')
  print('(V)ender produto ')
  print('(R)elatório de vendas ')
  print('(S)air ')
  print('*****************************')

  escolha = input('Informe sua opção: ').upper()
  return escolha

# Função principal

def principal():

  lista_vendas = []
  dic_produtos = {}

  while True:
    escolha = menu()

    if escolha == 'C':
      cad_produto(dic_produtos)

    elif escolha == 'L':
      listar_produtos(dic_produtos)

    elif escolha == 'V':
      venda(dic_produtos, lista_vendas)

    elif escolha == 'R':
      relatorio_vendas(dic_produtos, lista_vendas)

    elif escolha == 'S':
      break
