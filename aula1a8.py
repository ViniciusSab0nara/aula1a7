# -*- coding: utf-8 -*-
"""aula1a8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11VItvbKG9I8uh_rtqj24a1vfVRsACSnt
"""

texto = 'hello world'
print(texto)

contador = 10
while contador >= 1:
    print(contador)
    contador -= 1

print("fogo")

numero_real = 1.5
print(numero_real)

numero = 1
numero2 = 2
numero3= 3
cumprimento2 = 'ola, tudo bem?'

nome = input('digite o seu nome')
if(nome == 'vinicius'):
  print('Seja Bem Vindo')
else:
  print('usuario nao existe')

##1 -
##Crie um programa para efetuar a leitura de um número inteiro e apresentar o resultado do quadrado deste número.

numero = 10
print( 'o quadrado desse numero é', numero * numero)

##2 -
##Crie duas variáveis para armazenar seu primeiro nome e sobrenome. Em seguida, concatene-as para formar seu nome completo e exiba o resultado.

primeiroNome = 'Vinícius'
segundoNome = 'Sabonara'

print(primeiroNome + ' ' + segundoNome)

##3 -
##Peça ao usuário para digitar dois números inteiros e armazene-os em variáveis. Realize a concatenação desses números como strings e exiba o resultado.

numero1 = input('digite um numero inteiro')
numero2 = input('digite mais um numero inteiro')

print(numero1 +' '+ numero2)

##4 -
##Crie uma variável para armazenar a palavra "Python". Em seguida, adicione um número inteiro ao final da palavra usando a concatenação e exiba o resultado.

palavra = "Python"
numero = input('escolha um numero')

print(palavra + numero)

##5 -
##Declare uma variável contendo uma frase. Em seguida, peça ao usuário para digitar uma palavra e concatene essa palavra no final da frase. Exiba o resultado.

frase = "Meu nome é "
palavraEscolhida = input('qual o seu nome?')

print(frase + palavraEscolhida)

##6

##**Crie três variáveis para armazenar a quantidade de horas, minutos e segundos. Concatene esses valores para formar uma mensagem de tempo no formato "hh:mm:ss".**

hora = input("digite o horario 'hh'")
minuto = input("digite o minuto dessa hh")
segundo = input("digite os segundos")

print('agora são'+ ' ' + hora + ':' + minuto + ':' + segundo)



##7 -
##Declare duas variáveis com números de telefone, incluindo um código de área e o número principal. Concatene esses valores para formar um número de telefone completo.

telefone1 = 998279934
telefone2 = 974459334

##nao consegui interpretar

##8 -
##Crie uma lista de ingredientes para uma receita. Use concatenação para formar uma única string que liste os ingredientes separados por vírgulas.

ingrediente1 = input(" digite aqui o primeiro ingrediente")
ingrediente2 = input(" digite aqui o segundo ingrediente")
ingrediente3 = input(" digite aqui o terceiro ingrediente")
ingrediente4 = input(" digite aqui o quarto ingrediente")
ingrediente5 = input(" digite aqui o quinto ingrediente")

print("os ingredientes da receita são: ", ingrediente1 +','+ ingrediente2 +','+ ingrediente3 +','+ ingrediente4 + ','+ ingrediente5)

for n in range(2,20,2):
  print(n)

n1 = sum(range(1,101,))
print(n1)

# boas praticas ==
# listas com dados semelhantes
# . acessa propriedades da variavel remove()
# "len" comprimento da lista
#  del ("del list(0)")

list = [1,3,45,"b",55]
print(list[4])

list_numeros = [1,2,3,4,5]

print(list_numeros)

list_numeros = [1,2,3,4,5]

print(list_numeros[2])

# Remova o número 3 da lista numeros e imprima a lista resultante.
list_numeros = [1,2,3,4,5]
list_numeros.remove(3)


print(list_numeros)

list_numeros = [1,2,3,4,5]

list_seis = [6]

list_numeros.extend(list_seis)

print(list_numeros)

list_numeros = [1,2,3,4,5,6]

list_frutas = ["maça","banana","maçaneta"]

list_numeros.extend(list_frutas)

print(list_numeros)

list_numeros = [1,2,3,4,5,6]
list_frutas = ["maça","banana","mamão"]

list_numeros.extend(list_frutas)

frutas = 0

for frutas in list_frutas:
  print(frutas)

list_numeros = [1,3,6,5,25,16]

x = 0
for x in list_numeros:
  if x == 13:
    print(f'{x} está na lista')
  else:
    print('não tem nada aqui')

list_numeros = [1,3,6,5,25,16]

x = 0
for x in list_numeros:
  if x == 5:
    print(f'{x} está na lista')

tupla = (1,2,3,4,5,6)

n = tupla[0]

print(n)

lista = [1,2,3,4,5,6]

n = tuple(lista)

print(n)

##1 -  Crie uma tupla chamada frutas com pelo menos 5 frutas diferentes. Em seguida, acesse e imprima o terceiro elemento da tupla.

frutas = ("mamao", "maça", "banana", "abacate", "laranja", "uva")

lista_frutas =list(frutas)

lista_frutas.append("morango")
tupla_frutas = tuple(lista_frutas)

print(lista_frutas)
print(tupla_frutas)

##2 - Crie uma tupla chamada numeros com alguns números inteiros. Em seguida, converta essa tupla em uma lista e imprima a lista resultante.

numeros = (1,2,3,4,5,6,7,8)

numeros_lista = list(numeros)

print(numeros_lista)

##3 - Crie uma tupla chamada meses com os nomes dos meses do ano até Setembro. Use um loop for para imprimir cada mês em uma linha separada.

calendario = ("janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro")

for x in calendario:
 print(x)

##4 - Crie uma lista chamada notas com algumas notas de alunos. Em seguida, converta essa lista em uma tupla e imprima a tupla resultante.

notas = [10,8,5,6,7,2]

notas_tuple = tuple(notas)
print(notas)
print(notas_tuple)

##5 - Crie uma lista chamada ponto que represente as coordenadas (x, y) de um ponto. Em seguida, desempacote os elementos da lista em duas variáveis separadas (x e y) e imprima os valores.

ponto = ["lucas","luiz"]

x,y = ponto

print("coordenada", x)
print("coordenada", y)