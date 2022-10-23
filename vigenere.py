alpha_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Função para converder lista de numeros para uma variavel string
def toText(list):
  conv_text_list = []
  for c in list:
    for i in range(0, len(alpha_list)):
      if c == i:
        conv_text_list.append(alpha_list[i])
  conv_text = ""
  for i in conv_text_list:
      conv_text += str(i).upper()
  return conv_text

# Função para criptografar
def encrypt(text, key):
  for i in range(0, len(text)):
    crypt = text[i] + key[i]  
    if crypt >= 26:
      crypt %= 26
    crypt_list.append(crypt)
  crypt_text = toText(crypt_list)
  return print(f'Seu texto: \n{crypt_text}')

# Função para Descriptografar
def decrypt(text, key):
  for i in range(0, len(text)):
    plain = text[i] - key[i] + 26
    if plain >= 26:
      plain %= 26
    plain_list.append(plain)
  plain_text = toText(plain_list)
  print(".")
  return print(f'Seu texto: \n{plain_text}')

def toInt(txt):
  txt.lower()
  int_list = []
  for c in txt:
    for i in range(0, len(alpha_list)):
      if c == alpha_list[i]:
        int_list.append(i)
  return int_list

def space():
  for i in range(1, 10):
    print(".")

# Inicio do Programa
j=1
while j != 0:
  text_int = []
  key_int = []
  crypt_list = []
  plain_list = []
  print("="*25)
  print("Digite para:")
  print("1. Criptografar \n2. Descriptografar \n0. Sair do programa")
  quest = int(input("Resposta: "))
  if quest == 0:
    space()
    print("Saindo...")
    space()
    j=0
  elif quest == 1:
    print(".")
    h=1
    while h!=0:
      # Entrada de dados
      space()
      text = input("Texto que deseja criptografar: ")
      key = input("Chave: ")
      text = text.lower()
      key = key.lower()
      #Transformando texto e chave em numeros
      text_int = toInt(text)
      key_int = toInt(key)

      #verificação do tamanho da chave *
      if len(key_int) > len(text_int):
        print("Chave maior que texto")
        print(".")
      else:
        h = 0
    if len(text_int) > len(key_int):
      key_int_clone = key_int.copy()
      for i in range(0, len(text_int), len(key_int_clone)):
        key_int.extend(key_int_clone)
    encrypt(text_int, key_int)
    print(".")
    print("_"*25)
    print("1. Voltar\n0. Sair do programa")
    quest2 = int(input("Resposta: "))
    if quest2 == 0:
      j = 0
    print("=" *32)
    space()

  elif quest == 2:
    print(".")
    h=1
    while h!=0:
      # Entrada de dados
      space()
      text = input("Texto que deseja Descriptografar: ")
      key = input("Chave: ")
      text = text.lower()
      key = key.lower()
      print(text)
      #Transformando texto e chave em numeros
      text_int = toInt(text)
      key_int = toInt(key)

      #verificação do tamanho da chave *
      if len(key_int) > len(text_int):
        print("Chave maior que texto")
        print(".")
      else:
        h = 0
    if len(text_int) > len(key_int):
      key_int_clone = key_int.copy()
      for i in range(0, len(text_int), len(key_int_clone)):
        key_int.extend(key_int_clone)
    decrypt(text_int, key_int)
    print(".")
    print("_"*25)
    print("1. Voltar\n0. Sair do programa")
    quest2 = int(input("Resposta: "))
    if quest2 == 0:
      j = 0
    print("=" *32)
    space()