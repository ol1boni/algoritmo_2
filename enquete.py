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