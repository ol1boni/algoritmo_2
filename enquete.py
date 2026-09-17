def cadastrar_opcao (opcoes,votos):
  nome = input("Digite o nome da nova opção: ")
  opcoes.append(nome)
  votos.append(0)
  print("Opção cadastrada com sucesso")

def listar_opcoes(opcoes):
  if len(opcoes) == 0:
    print("Nenhuma opção cadastrada ainda.")
    return
  print("----Opções cadastradas----")