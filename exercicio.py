Exercícios:

# 1 - Escreva um programa que leia o nome de um funcionário,
# seu número de horas trabalhadas, o valor que recebe por hora
# e calcula o salário desse funcionário.
# A seguir, mostre o nome e o salário do funcionário.

nome_funcionario = input('Digite seu nome')
horas_trabalhadas = int(input('Digite o numero de hras trabalhadas'))
valor_hora = float(input('Digite o valor que recebe por hora'))
calcula_salario = (horas_trabalhadas * valor_hora)

print (f'{nome_funcionario} seu salario é de: {calcula_salario}')


# 2 - crie uma função que receba uma lista de 20 valores aleatórios, retornar
# apenas o maior valor e printar em tela.

import random

contador = 0
aleatorio = [ ]

while contador < 20:
        aleatorio.append(random.randrange(0,20))
        contador +=1

maior = max(aleatorio)

print(aleatorio)
print(f'O maior numero da lista é: {maior}')

# 3 - crie uma lista com 10 números aleatórios,
# itere essa lista e printar em tela os
# valores que são ímpares e pares.

import random

contador = 0
aleatorio = [ ]
pares = []
impares = [ ]

while contado < 10:
        aleatorio.append(random.randrange(0,20))
        contador +=1

for i in aleatorio:
        if 1%2 == 0:
            pares.append(i)

        else:
            impares.append(i)

print(f'Essa é sua lista: {aleatorio}')
print(f'Impares: {impares}')
print(f'Pares: {pares}')


# 4 - Crie uma função python que cálcule uma função de 2º Grau

a = int(input('valor de a: '))
b = int(input('valor de b: '))
c = int(input('valor de c: '))

def bhaskara(a, b, c):
    delta = (b*b) - (4(a*b))
    bask = ((-b) + (delta)**(1/2)) / (2*a))
    bask2 =((-b)) - (delta)**(1/2) / (2*a))
    print('Bhaskara positivo ++ :',bask)
    print('Bhaskara negativo -- :', bask2)

bhaskara(a,b,c)

# 5 - Faça um programa que leia o raio de um círculo e faça duas
# funções: uma que calcule a área do círculo e outra que calcule
# o comprimento do círculo.

raio = int(input('Qual o raio do círculo: '))
meu_nome = input('Seu nome: ')
def hello(meu_nome):
    print('Olá', meu_nome)

def calculo (raio):
    area = (raio**2) * 3.14
    return area

raio_circulo = float(input('Digite o raio do crculo: '))
pi = 3.14

def calcula_area(raio_circulo, pi):
    area = (pi * (raio_circulo ** 2))
    print('Area do círculo é: {}m²' .format(area))

calcula_area(raio_circulo, pi)

def calcula_comprimento(raio_circulo. pi):
    comprimento = (2*pi * raio_circulo)
    print('Comprimento do circulo é {}m' .format(comprimento))

calcula_comprimento(raio_circulo, pi)
