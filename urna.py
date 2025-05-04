def lista_cand(dict_cand):
    print('\n'*100)
    print('Candidatos:')
    for numero, nome in dict_cand.items():
        print(numero, '-', nome)

def adiciona_cand(dict_cand):
    lista_cand(dict_cand)
    print('\nInforme os dados do novo candidato')
    num = input('Número: ')
    nome = input('Nome: ')
    if len(num) != 2 or not num.isdigit() or num in dict_cand:
        print('Cadastro inválido!')
    else:
        dict_cand[num] = nome

def pega_voto(dict_cand, dict_votos):
    while True:
        lista_cand(dict_cand)
        print('\nInforme seu voto')
        voto = input('Número do candidato: ').strip()
        if voto == '':
            voto = 'Branco'
        elif voto in dict_cand:
            voto = voto + ' - ' + dict_cand[voto]
        else:
            voto = 'Nulo'
        print('Voto:', voto)
        resp = input('Confirma (S/N): ').lower().strip()
        if resp == 's':
            soma_voto(dict_votos, voto)
            break

def soma_voto(dict_voto, voto):
    if voto in dict_voto:
        dict_voto[voto] += 1
    else:
        dict_voto[voto] = 1

def principal():
    dict_cand = {}
    while True:
        adiciona_cand(dict_cand)
        resp = input('Continuar cadastros (S/N): ').lower().strip()
        if resp == 'n':
            break
        dict_voto = {}
        total = 0
        while True:
            pega_voto(dict_cand, dict_voto)
            total += 1
            resp = input('Encerrar votação (S/N): ').lower().strip()
            if resp == 's':
                break
            print('Resultado da eleição:')
            for voto in dict_voto:
                porcent = round(dict_voto[voto] / total * 100, 2)
                print(voto, ': ', dict_voto[voto],' (', porcent, '%', ')', sep='')

if __name__ == '__main__':
    principal()