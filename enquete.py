def cadastrar_opcao (opcoes,votos):
  nome = input("Digite o nome da nova opção: ")
  opcoes.append(nome)
  votos.append(0)
  print("Opção cadastrada com sucesso")

def listar_opcoes(opcoes):
    if len(opcoes) == 0:
        print("Nenhuma opção cadastrada ainda.")
        return

    print("----- Opções cadastradas -----")
    for i in range(len(opcoes)):
        print(i, "-", opcoes[i])

def registrar_voto(opcoes, votos):
    if len(opcoes) == 0:
        print("Não há opções cadastradas para votar.")
        return

    listar_opcoes(opcoes)
    posicao = int(input("Digite o número da opção que deseja votar: "))

    if posicao < 0 or posicao >= len(opcoes):
        print("Opção inválida.")
    else:
        votos[posicao] = votos[posicao] + 1
        print("Voto registrado em:", opcoes[posicao])

def consultar_quantidade_votos(opcoes, votos):
    if len(opcoes) == 0:
        print("Não há opções cadastradas.")
        return

    listar_opcoes(opcoes)
    posicao = int(input("Digite o número da opção: "))

    if posicao < 0 or posicao >= len(opcoes):
        print("Opção inválida.")
    else:
        print(opcoes[posicao], "possui", votos[posicao], "voto(s).")

def mostrar_resultado(opcoes, votos):
    if len(opcoes) == 0:
        print("Não há opções cadastradas.")
        return
    
    total = 0
    for v in votos:
        total = total + v
    print ("---- Resultado da enquete ----")
    
    if total == 0:
        print("Ainda não há votos registrados.")
        return
    
    for i in range(len(opcoes)):
        percentual = (votos[i] / total) * 100
        print(opcoes[i], "-", votos[i], "voto(s) -", round(percentual, 2), "%")
        
    print("Total de votos:", total)

def mostrar_vencedora(opcoes, votos):
    if len(opcoes) == 0:
        print("Não há opções cadastradas.")
        return
    
    maior = votos[0]
    for v in votos:
        if v > maior:
            maior = v
    
    if maior == 0:
        print("Ainda não há votos registrados.")
        return
    
    vencedoras = []
    for i in range(len(votos)):
        if votos[i] == maior:
            vencedoras.append(opcoes[i])
    
    if len(vencedoras) == 1:
        print("A opção vencedora é:", vencedoras[0], "com", maior, "voto(s).")
    else:
        print("Houve um empate entre as opções:")
        for nome in vencedoras:
            print("-", nome)
        print("Cada uma com", maior, "voto(s).")


def mostrar_menu():
    print("\n========= ENQUETE =========")
    print("1 - Cadastrar opção")
    print("2 - Listrar opções")
    print("3 - Registrar voto")
    print("4 - Consultar quantidade de votos")
    print("5 - Mostrar resultado")
    print("6 - Mostrar opção vencedora")
    print("7 - Encerrar")


opcoes = []
votos = []
opcao_escolhida = 0

while opcao_escolhida != 7:
    mostrar_menu()
    opcao_escolhida = int(input("Digite a opção desejada: "))