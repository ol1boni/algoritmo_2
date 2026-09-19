opcoes = [] # cria lista vazia para armazenar os nomes das opções cadastradas
votos = [] # cria uma lista vazia para armazenar a contagem de votos de cada opção

def cadastrar_opçao(opcoes, votos): # é onde as opções sao cadastradas
  opcao = input("Digite a opção que deseja cadastrar: ")
  if opcao in opcoes: # verifica se a opcao digitada ja existe dentro da lista (opcoes)
    print("Opção já cadastrada.")
  else:
    opcoes.append(opcao) # adiciona o nome ao final da lista (opcoes)
    votos.append(0) # Adiciona o valor 0 ao final da lista votos e inicia o contador de votos para essa nova opção
    print("Opção cadastrada com sucesso.")

def listar_opcoes(): # função para exibir todas as opções cadastradas
    for i in opcoes: # Percorre cada item dentro da lista opcoes e guarda o valor atual na variável i
        print(i) 

def registrar_voto(opcoes, votos): # função reponsavel por add um voto
  listar_opcoes() # chama a função que mostra as opções disponiveis (pra facilitar a escolha)
  opcao = input("Digite a opção que deseja votar: ") 
  if opcao in opcoes: # verifica se a opção digitada realmente existe na lista
    voto = opcoes.index(opcao) # busca o índice da opção escolhida na lista opcoes
    votos[voto] += 1 #  aumentar o número de votos 
    print("Voto registrado com sucesso.")
  else:
    print("Opção inválida.")

def consultar_votos(opcoes, votos): # função para verificqar os votos de uma opção especifica
  opcao = input("Digite a opção que deseja consultar os votos: ")
  if opcao in opcoes: # verifica se a opção digitada está cadastrada
    voto = opcoes.index(opcao) #  busca o índice da opção escolhida na lista opcoes
    print(f"A opção '{opcao}' possui {votos[voto]} votos.")
  else:
    print("Opção inválida.")

def mostrar_resultado(opcoes, votos): # mostra o balanço geral da votação
  total_votos = sum(votos) # soma todos os números contidos na lista votos e guarda na variável total_votos

  if total_votos == 0:
    print("Nenhum voto registrado.")
    return
  for i in range(len(opcoes)): # contar os votos de todas as opções para fazer o percentual
     percentual_votos = votos[i]/total_votos * 100
     print(f"{opcoes[i]} - {percentual_votos:.2f}% - {votos[i]} votos")

def mostrar_vencedora(opcoes, votos): # define a função que calcula quem ganhou
  total_votos = sum(votos) # calcula a soma de todos os votos do sistemas
  vencedora = [] # cria lista vazia para armazenar os vencedores
  if len(opcoes) == 0: 
     print("Nehuma opção cadastrada.")
     return
  if total_votos == 0:
    print("Nenhum voto registrado.")
    return
  for i in range(len(opcoes)): 
    if votos[i] == max(votos): # guarda o maior voto e verifica se teve empate
      vencedora.append(opcoes[i]) # adiciona na lista 
  if len(vencedora) == 1: # se houver somente um vencedor
    print(f"A opção vencedora é: {vencedora[0]}")
  else: 
    print("Houve um empate entre as opções: ")
    for i in vencedora:
      print(i)
def menu():
  while True:
      print("1. Cadastrar opção")
      print("2. Listar opções")
      print("3. Registrar voto")
      print("4. Consultar votos")
      print("5. Mostrar resultado")
      print("6. Mostrar vencedora")
      print("7. Encerrar votação")
      escolha = input("Escolha uma opção de 1 a 7: ")
      if escolha == '1':
          cadastrar_opçao(opcoes, votos)
      elif escolha == '2':
          listar_opcoes()
      elif escolha == '3':
          registrar_voto(opcoes, votos)
      elif escolha == '4':
          consultar_votos(opcoes, votos)
      elif escolha == '5':
          mostrar_resultado(opcoes, votos)
      elif escolha == '6':
          mostrar_vencedora(opcoes, votos)
      elif escolha == '7':
          print("Votação encerrada")
          break
      else:
          print("Opção inválida. Tente novamente.")

menu()