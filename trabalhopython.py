def menu(lista):
    print('### Menu aluno ###')
    print('# 1 - cadastrar # ')
    print('# 2 - remover # ')
    print('# 3 - listar # ')
    print('# 4 - atualizar # ')
    print('# 5 - fechar # ')
    print(' ### ------ ### ')

    tipo = int(input("Digite a operação: "))

    if tipo == 1:
        cadastrar(lista)
    elif tipo == 2:
        remover(lista)
    elif tipo == 3:
        listar(lista)
    elif tipo == 4:
        atualizar(lista)
    elif tipo == 5:
        fechar(lista)
    else:
        print('Operação inválida')
        menu(lista)

def cadastrar(lista):
    print('### Operação Cadastrar ###')

    id      = input("Id: ")
    nome    = input("Nome: ")
    idade   = int(input("Idade: "))
    rg      = input("RG: ")

    save(lista, id, nome, idade, rg)
    print('Aluno cadastrado com sucesso!')

    verificacao = int(input("Gostaria de cadastrar uma novo aluno? [1-Sim/2-Não]: "))
    if verificacao == 1:
        cadastrar(lista)

    elif verificacao == 2:
        menu(lista)

    else:
        print("Opção Inválida!")
        menu(lista)


def atualizar(lista):
    chave = input('Digite o código do aluno: ')

    for dados in lista:
        if dados['id'] == chave:
            dados['nome']      = input('Nome: ')
            dados['idade']     = int(input('Idade: '))
            dados['rg']        = input('RG: ')

    print('Dados do aluno atualizados com sucesso!')

    menu(lista)


def remover(lista):
    id = input("Digite o código do aluno a ser removido: ")

    contador = 0
    while contador < len(lista):
        if lista[contador]['id'] == id:
            del lista[contador]
            print('O aluno foi removido com sucesso!')
        

        contador += 1

    menu(lista)

def listar(lista, verificacao=0):
    print('### Listagem ###')

    for dados in lista:
        print(dados['id'] + ', ' + dados['nome'] + ', ' + str(dados['idade']) + ', ' + dados['rg'])

    if verificacao == 1:
        print('Programa finalizado')
    else:
        menu(lista)

def fechar(lista):
    listar(lista, 1)

def save(lista, id, nome, idade, rg):
    lista.append({
        'id'    : id,
        'nome'  : nome,
        'idade' : idade,
        'rg'    : rg
    })

if __name__== '__main__':
    lista = []
    menu(lista)
