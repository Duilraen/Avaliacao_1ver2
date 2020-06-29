class Telefone():
  def __init__(self, nome, telefone):
    self.__nome = nome
    self.__telefone = telefone

  def getNome(self):
    return self.__nome
  
  def getTelefone(self):
    return self.__telefone
