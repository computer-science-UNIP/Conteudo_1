nova_aula = "Física é legal "

print(len(nova_aula)) # no caso de strings, faz a contagem de caracteres
print(nova_aula[1]) # retorna o caractere na posição do respectico índice
# o que acontece se passarmos a quantidade de caracteres da string?

print(nova_aula[2:4]) # considera o primeiro índice, mas não o último!
print(nova_aula[-5:-2])

print(nova_aula.index("é")) # posição da string ou caractere # o primeiro índice a aparecer

# e se buscarmos um texto que não existe?

# verificar, primeiro, se o texto está contido na variável

b = "é" in nova_aula

print(f"A busca retornou: {b}")

múltiplas_linhas1 = """linha 1
linha 2
linha 3
"""

print(múltiplas_linhas1)

# utilizar também o caractere de escape para uma nova linha: \n


múltiplas_linhas2 = "linha 1 \nlinha 2 \nlinha 3"
print(múltiplas_linhas2)