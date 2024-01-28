def imprimir_piramide(n):
  for i in range(1, n + 1):
      espacos = " " * (n - i)
      if i == 1:
          linha = espacos + "*"
      else:
          linha = espacos + "*" + " " * (2 * (i - 2) + 1) + "*"
      print(linha)

# Defina o número de linhas desejado
numero_linhas = 10

# Chame a função para imprimir a pirâmide
imprimir_piramide(numero_linhas)

