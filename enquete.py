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


while escolha != 7:
    escolha = int(input("Digite um dos seguintes números para escolher uma opção: \n 1. Cadastrar Opção. \n 2. Listar Opções. \n 3. Registrar Voto \n 4. Consultar Quantidade de Votos. \n 5. Mostrar Resultado. \n 6. Mostrar Opção Vencedora \n 7. Encerrar \n\n> "))
    if escolha == 1:
        cadastrar_opcao(opcoes, votos)
    elif escolha == 2:
        print(f"lista atual de opções: {opcoes}\n")
    elif escolha == 3:
        registrar_voto(opcoes, votos)
    elif escolha == 4:
        print(f"{sum(votos)} votos totais.")
    elif escolha == 5:
        if len(opcoes) == 0:
            print("Nenhuma opção válida registrada.")
        elif sum(votos) == 0:
            print("Nenhum voto válido registrado")
        else:
            print("Nenhuma opção válida registrada.")
    elif escolha == 6:
        if len(opcoes) == 0:
            print("Nenhuma opção válida registrada.")
        elif sum(votos) == 0:
            print("Nenhum voto válido registrado")
        else:
            mostrar_vencedor(opcoes, votos)
    elif escolha == 7:
        print("Encerrando o programa...")
    else:
        print("Opção Inválida!")