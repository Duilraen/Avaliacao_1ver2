from Controller import Controller
agenda = []
print('-----------Contatos-----------')
while True:
  print('1 - Novo contato; ')
  print('2 - Apagar contato; ')
  print('3 - Buscar todos os contatos; ')
  print('4 - Apagar todos os contatos; ')
  print('5 - Sair.')
  opcao = int(input('Selecione a opção: '))
  if opcao == 1:
    nome = input('Digite o nome: ')
    tel = int(input('Digite o telefone: '))
    agenda.append(Controller.inserir(nome, tel))
  elif opcao == 2:
    nome = input('Digite o nome para a pesquisa: ')
    print(Controller.deletarNome(agenda, nome))
  elif opcao == 3:
    Controller.listarAll(agenda)
  elif opcao == 4:
    print(Controller.deletarAll(agenda))
  elif opcao == 5:
    break
  else:
    print('Digite a opção disponivel!')
print('-----------Encerrando-----------')
