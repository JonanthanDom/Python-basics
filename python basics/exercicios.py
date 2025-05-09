# Desafio 01: Criar um script python que leia o nome de uma pessoa 
# e mostre uma mensagem de boas-vindas de acordo com o valor digitado.
nome = input('Qual o seu nome?')
print('Bem vindo ' + nome + '!!!')

# Desafio 02: criar um script python que leia o dia, o mês e o ano de nascimento de uma pessoa 
# e mostre uma mensagem com a data formatada.
dia = input(nome + ', Qual o dia que você nasceu?')
mes = input('E o mês?')
ano = input('De qual ano?')
print('Dados atualizados!!! você nasceu em', dia, '/', mes, '/', ano)

# Desafio 03:  criar um script de python que leia dois números e 
# mostre o resultado da soma entre eles.
#recebe dois números inteiros
num1 = int(input('Qual o primeiro número da soma?'))
num2 = int(input('qual o segundo número da soma?'))
#realiza a operação de adição
soma = num1 + num2
#apresenta o resultado para o usuário
print('A soma entre {} e {} é igual a {}'.format(num1, num2, soma))

#Desafio 4:crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas
#informações sobre ele.
v = input('digite algo:')
print('O tipo primitivo desse valor é:', type(v))
print('é uma letra?', v.isalpha())
print('é um número?', v.isnumeric())
print('contém letras e números?', v.isalnum())
print('está em letras maiusculas?', v.isupper())
print('está em letras minpusculas?', v.islower())
print('Só tem espaços?', v.isspace())
print('Está capitalizado?', v.istitle())

#Desafio 5: Faça um programa que leia um nímero inteiro e 
# mostre na tela o seu sucessor e o seu antecessor
n = int(input("digite um número:"))
a = n - 1
s = n + 1
print('O número digitado foi {}, seu antecessor é {} e seu sucesor é {}'.format(n, a, s))

#Desafio 6:Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número:'))
d = n*2
t = n*3
r = n**0.5
print('o dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}.'. format(n, t))
print('A raz quadrada de {} vale {:.2f}.'. format(n, r))

#Desafio 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunta nota: '))
media = (n1 + n2)/2
print('A média do aluno é: {:.1f}'.format(media))

#Desafio 8:Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
d = float(input('Informe a distância em metros: '))
Km = d/1000
Hm = d/100
Dam = d/10
Dm = d*10
Cm = d*100
Mm = d*1000
print('A medida de {} em metros corresponde a: \n{}Km \n{}Hm \n{}Dam \n{:.0f}Dm \n{:.0f}cm \n{:.0f}Mm'.format(d, Km, Hm, Dam, Dm, Cm, Mm))

 #desafio 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
n = int(input('***Programa tabuada*** \n Digite um número para saber sua tabuada:'))
print('==========')
print('{} x  1 = {}'.format(n, n*1))
print('{} x  2 = {}'.format(n, n*2))
print('{} x  3 = {}'.format(n, n*3))
print('{} x  4 = {}'.format(n, n*4))
print('{} x  5 = {}'.format(n, n*5))
print('{} x  6 = {}'.format(n, n*6))
print('{} x  7 = {}'.format(n, n*7))
print('{} x  8 = {}'.format(n, n*8))
print('{} x  9 = {}'.format(n, n*9))
print('{} x 10 = {}'.format(n, n*10))
print('='*12)

#Desafio 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real = float(input('Quantos reais você tem? R$'))
dolar = real / 5.83
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))

#Desafio 11:Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
altura = float(input('Qual a altura da sua parede?'))
largura = float(input('Qual a largura da sua parede?'))
area = altura*largura
tinta = area/2
print('A sua parede tem {} de altura e {} de lagura com àrea de {:.2f}m². \npara pintar essa parede você precisará de {:.1f} litros de tinta'.format(altura, largura, area, tinta))

#Desafio 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, 
# com 5% de desconto.
preco = float(input('Qual o valor do produto: R$'))
desconto = preco - (preco / 20)
#outra fomra de fazer o calculo é:
#desconto = preço - (preco*5/100)
print('O valor com desconto de 5% é R${:.2f}'.format(desconto))

#Faça um algoritmo que leia o salário de um funcionário
#  e mostre seu novo salário, com 15% de aumento.
salario = float(input('Qual o salário a ser reajustrado? R$'))
novo = salario + (salario * 15 / 100)
print('O salário R${:.2f} com 15% de aumento será R${:.2f}'.format(salario, novo))

#Desafio 14:  Escreva um programa que converta uma temperatura digitando em graus Celsius 
# e converta para graus Fahrenheit.
celsius = float(input('Qual a temperatura em Celsius?'))
farenheit = (celsius * 1.8) + 32
print('A temperatura {}ºC é equivalente a {}ºF'.format(celsius, farenheit))

#Desafio 15:Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#  e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = float(input('Quantos dias o carro foi alugado?'))
km = float(input('Quantos Km foram percorridos?'))
total = (dias * 60) + (km * 0.15)
print('O valor total a pagar é: R${:.2f}' .format(total))

#Desafio 16: Crie um programa que leia um número Real qualquer pelo teclado ,
# e mostre na tela a sua porção Inteira.
from math import floor
num = float(input('Digite um núemro qualquer: '))
print('O número digitado foi {}, sua porção inteira é: {}'.format(num, floor(num)))

# Desafio 17: Faça um programa que leia o comprimento do cateto oposto
#  e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
catoposto = float(input('digite o comprimento do cateto oposto: '))
catadjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(catoposto, catadjacente)
print('A hipotenusa mede: {:.2f}'.format(hipotenusa))

#Desafio 18:Faça um programa que leia um ângulo qualquer e 
# mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import cos, tan, sin, radians
angulo = float(input('Digite o angulo que você deseja: '))
radi = radians(angulo)
sen = sin(radi)
coss = cos(radi)
tang = tan(radi)
print('O angulo de {}, tem o seno de: {:.2f}'.format(angulo, sen))
print('O angulo de {}, tem o cosseno de: {:.2f}'.format(angulo, coss))
print('O angulo de {}, tem a tangente de: {:.2f}'.format(angulo, tang))

#Desafio 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
aluno1 = input('digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.choice(lista)
print('O aluno escolhido foi: {}'.format(sorteio))

#Desafio 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos
#  dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import sample
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista =[a1, a2, a3, a4]
ordem = sample(lista, k=4)
print('A ordem de apresentação será: \n {}'.format(ordem))

#desafio 22: crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas as letras maiusculas e minusculas
#a quantidade de letras, sem contar os espaços
#quantas letras tem o primeiro nome
name = input('Digite seu nome: ').strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é: ', name.upper())
print('Seu nome em minúsculs é: ', name.lower())
print('Seu nome tem ao todo {} letras'. format(len(name) - name.count(' ')))
name = name.split()
print('Seu primeiro nome é: {} e ele tem {} letras.'.format(name[0], len(name[0])))

#Desafio 23: Faça um programa que leia um número de 0 a 9999 
# e mostre na tela cada um dos dígitos separados.
number = int(input('digite um número entre 0 e 9999: '))
u = number // 1 % 10
d = number // 10 % 10
c = number // 100 % 10
m = number // 1000 % 10
print('Analisando o npumero: {}'.format(number))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'. format(c))
print('Milhar: {}'.format(m))

#Desafio 24: Crie um programa que leia o nome de uma cidade diga
#  se ela começa ou não com o nome “SANTO”.
name = input('Digite a cidade que você nasceu: ').strip()
name = name.upper()
name = name.split()
valor = name[0] == 'SANTO'
print(valor)

#crie umn programa que leia um nome e diga se ela tem silva no nome:
name = input('Digite seu nome: ').strip()
name = name.upper()
name = name.split()
if "SILVA" in name: 
    print('Seu nome tem silva')
else:
    print('Seu nome não tem silva')
#refatorando:
name = input('Digite seu nome: ').strip()
print('Seu nome tem silva? {}'.format('silva' in name.lower()))

#Desafio 26: Faça um programa que leia uma frase pelo teclado e 
# mostre quantas vezes aparece a letra “A”, 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).strip()
frase = frase.upper()
a = frase.count('A')
print('A letra A aparece {} vezes na frase.'.format(a))
print('A letra A aparece pela primeira vez na posição {}.'.format(frase.find('A')+ 1) ) #busca a posição da primeira letra A
print('A letra A aparece a ultima vez na posição: {}'.format(frase.rfind('A') +1 )) #busca a posição agora de tras pra frente.

# Desafio 27: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
nome = input('Digite seu nome: ').strip()
nome = nome.split()
print('Prazer em te conhecer!!!!')
print('A primeira palavra do seu nome é: {}'.format(nome[0]))
print('A ultima letra do seu nome é: {}'.format(nome[-1]))

#Desafio 28:  Escreva um programa que faça o computador “pensar” em um número inteiro
#  entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#  O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
num = randint(0, 5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('-=-'*20)
palpite = int(input('Em qual número estou pensando?'))
print('PROCESSANDO...')
sleep(2) #faz o computador esperar antes de executar o próximo bloco
if palpite == num:
    print('Parabéns!!!!! o número foi {}'.format(num))
else:
    print('Errou!!!!!!! eu pensei em {}'. format(num))

#Desafio 29: Escreva um programa que leia a velocidade de um carro.
#  Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#  A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input('Qual a velocidade do carro?'))
if velocidade >= 81:
    multa = (velocidade - 80)*7
    print('VOCÊ EXCEDEU O LIMITE DE 80Km/h!')
    print('Deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha uma ótima viagem!')

#Desafio 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Escreva um número:'))
if num % 2 == 0:
    print('O número é par!')
else:
    print('O número é impar')

#Desafio 31:  Desenvolva um programa que pergunte a distância de uma viagem em Km.
#  Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km 
# e R$0,45 parta viagens mais longa
from time import sleep
print('-=-'*20)
distancia = int(input('Qual a distância da sua viagem? '))
print('-=-'*20)
print('você está prestes a iniciar uma viagem de: {} km, só um minuto enquanto calculamos a sua passagem.' .format(distancia))
sleep(3)
if distancia <= 200:
    preco  = distancia * 0.50
    print('Sua passagem custa: {:.2f}'.format(preco))
else:
    preco = distancia * 0.45
    print('Sua passagem custa {:.2f}'.format(preco))

#Desafio 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import calendar
from datetime import datetime
ano = int(input('Digite um ano para saber se ele é bissexto, ou digite 0 para o ano atual:'))
if ano == 0:
    ano = datetime.now().year
if calendar.isleap(ano):
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'. format(ano))

#Desafio 33:Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
maior = max(n1, n2, n3)
menor  = min(n1, n2, n3)
print('O maior valor é: {}'. format(maior))
print('O menor valor é: {}'.format(menor))

#Desafio 34: Escreva um programa que pergunte o salário de um funcionário e 
# calcule o valor do seu aumento.
#  Para salários superiores a R$1250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Reajuste salarial. \n digite o salário do funcionário: R$'))
if salario <= 1250.00:
    novo_salario = salario + (salario * 15 /100)
else:
    novo_salario = salario + (salario * 10/100)
print('QUem recebia R${:.2f} passa a receber R${:.2f}'.format(salario, novo_salario))

#Desafio 35:Desenvolva um programa que leia o comprimento de três retas
#  e diga ao usuário se elas podem ou não formar um triângulo.
print('-=-'*20)
print('ANALISADOR DE TRIANGULOS')
print('-=-'*20)
s1 = float(input('Digite o valor do primeiro segmento:'))
s2 = float(input('Digite o valor do segundo segmento: '))
s3 = float(input('Digite o valor do terceiro segmento: '))
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print('Os segmentos acima podem formar um triangulo')
else:
    print('Os segmentos acima não podem formar um triangulo.')

#Desafio 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#  Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
print('=-='*30)
print('Simulador de financiamento residencial ')
print('=-='*30)
valorCasa = float(input('qual o valor do imóvel? R$'))
salario = float(input('Qual o seu salário?'))
tempo = float(input('De quantos anos será o financiamento?'))*12
mensalidade = valorCasa / tempo
if mensalidade > (salario * 30/100):
    print('Para comprar uma casa de {:.0f} em {:.0f} meses, o valor da prestação será {:.2f}'.format(valorCasa, tempo, mensalidade))
    print('por isso o empréstimo não foi aprovado.')
else:
    print('Para comprar uma casa de {:.0f} em {:.0f} meses, o valor da prestação será {:.2f}'.format(valorCasa, tempo, mensalidade))
    print('Empréstimo aprovado, parabéns!!!!')

#Desafio 37: Escreva um programa em Python que leia um número inteiro qualquer 
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 
# 2 para octal e 
# 3 para hexadecimal.
numero = int(input('Digite um número para conversão: '))
opcao = int(input('Agora escolha a base para conversão: \n [1] para codigo BINARIO \n [2] para OCTAL \n [3] para HEXADECIMAL '))
if opcao == 1:
    print('Voce selecionou a opção BINARIO:')
    binario = bin(numero)[2:]
    print(binario)
elif opcao ==2:
    print('Você selecionou a opção OCTAL:')
    octal = oct(numero)[2:]
    print(octal)
elif opcao == 3:
    print('Você selecionou a opção HEXADECIMAL:')
    hexadecimal = hex(numero)[2:].upper()
    print(hexadecimal)
else:
    print('Opção inválida!!! \nencerrando programa')

#Desafio 38: Escreva um programa que leia dois números inteiros e compare-os.
#  mostrando na tela uma mensagem:
# O primeiro valor é maior, o segundo valor é maior ou os dois valores são iguais
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O primeiro número é maior')
elif n2 > n1:
    print('O segundo número é maior')
else:
    print('os dois números são iguais')

# Desafio 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
#  de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import datetime
ano_nascimento = int(input('Qual o ano que você nasceu?'))
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento
print('em {}  você terá {} anos'.format(ano_atual, idade))
if idade < 18:
    tempo_restante = 18 - idade
    print('você deverá se alistar daqui a {} anos'.format(tempo_restante))
    print('Seu alistamento será em {}'.format(ano_atual + tempo_restante))
elif idade > 18:
    tempo_restante = idade - 18
    print('Você passou do prazo de alistament a {} anos, compareça ao serviço militar!'.format(tempo_restante))
    print('Seu alistamento deveria ter sido em {}'.format(ano_atual - tempo_restante))
else:
    print('você deve se alistar imediatamente!')

#Desafio 40: Crie um programa que leia tres notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media = (n1 + n2 + n3) / 3
if media >= 7.0:
    print('A média foi {}, você está aprovado!'.format(media))
elif media < 5.0:
    print('Sua média foi {}, você está reprovado!'.format(media))
else:
    print('Sua média foi {}, você vai para a recuperação.'.format(media))

#Desafio 41: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
#  de um atleta e mostre sua categoria, de acordo com a idade:
# 9 anos mirim
# 14 anos infantil
# 19 anos junior
#25 anos senior
# acima de 25 anos master
from datetime import datetime
nasc = int(input('Digite o ano do seu nascimento: '))
ano = datetime.now().year
idade = ano - nasc
print('O atleta tem {} anos.'.format(idade))
if idade >= 26:
    print('Classificação: MASTER')
elif idade >= 19:
    print('Classificação SENIOR')
elif idade >= 14:
    print('Classificação JUNIOR')
elif idade >= 9:
    print('Classificação INFALTIL')
else:
    print('CLassificação MIRIM')

#Desafio 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de 
# triângulo será formado:
#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes
print('-=-'*20)
print('ANALISADOR DE TRIANGULOS')
print('-=-'*20)
s1 = float(input('Digite o valor do primeiro segmento:'))
s2 = float(input('Digite o valor do segundo segmento: '))
s3 = float(input('Digite o valor do terceiro segmento: '))

if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1 and s1 == s2 == s3:
    print('o triangulo formado será do tipo EQUILÁTERO.')
elif s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1 and s1 == s2 or s1 == s3 or s2 == s3:
    print('O triangulo formado será do tipo ESCALENO')
elif s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1 and s1 != s2 != s3:
    print('O trinagulo formado será do tipo ISÓSCELES')
else:
    print('OS segmentos acima não podem fomrar um triangulo.')

'''Desafio 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
IMC abaixo de 18,5: Abaixo do Peso
Entre 18,5 e 25: Peso Ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade Mórbida'''
peso = float(input('Qual o seu peso em kg? '))
altura = float(input('Qual a sua altura em metros? '))
imc = peso / altura**2
if imc < 18.5:
    print('Seu imc é {:.2f}, \nvocê está abaixo do peso ideal'. format(imc))
elif 18.5 <= imc < 25.0:
    print('Seu imc é {:.2f}, \nvocê está no peso ideal.'.format(imc))
elif 25.0<= imc < 30:
    print('Seu imc é {:.2f}, \nvocê está em sobrepeso.'.format(imc))
elif 30<= imc < 40.0:
    print('Seu imc é {:.2f}, \nvocê está obeso.'.format(imc))
else:
    print('Seu imc é {:.2f}, \nvocê está com obesidade mórbida!!!'.format(imc))

'''Desafio 44:  Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço formal 
3x ou mais no cartão: 20% de juros'''
print('='*20, 'CAIXA', '='*20)
compras = float(input('Digite o valor total das compras: R$'))
forma_pgto = int(input('''              FORMAS DE PAGAMENTO
            [ 1 ] À VISTA EM DINHEIRO
            [ 2 ] DÉBITO / CRÉDITO À VISTA
            [ 3 ] PARCELADO \n'''))
if forma_pgto == 1:
    print('Pagamento à vista em dinheiro.')
    compras = compras - (compras *10 /100)
    print('O total a pagar será R${:.2f} com desconto de 10%'.format(compras))
elif forma_pgto == 2:
    print('Pagamento à vista no cartão débito / crédito.')
    compras = compras - (compras * 5 / 100)
    print('O total a pagar será R${:.2f} com desconto de 5%'.format(compras))
elif forma_pgto == 3:
    print('Pagamento parcelado.')
    parcelas = int(input('Qual a quantidade de parcelas? '))
    if parcelas <= 2:
        print('''Você vai pagar {}x de {:.2f},
              total R${:.2f} sem descontos'''.format(parcelas, (compras / parcelas), compras))
    elif parcelas > 2:
        juros = compras + (compras *20 / 100)
        print('''Você vai pagar {}x de {:.2f} com juros de 20%.
              Sua compra de R${:.2f} vai custar R${:.2f}.'''.format(parcelas, (juros/ parcelas), compras,  juros))

'''Desafio 45: Crie um programa que faça o computador jogar Jokenpô com você.'''
import random
from time import sleep
lista = ['pedra', 'papel', 'tesoura']
print('=-=' *10, ' PEDRA PAPEL TESOURA', '=-='*10)
print('''Suas opções:
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA''')
palpite = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sorteio = random.choice(lista)
print('='*40)
print('O computador jogou {}'.format(sorteio))
print('Você jogou {}'.format(lista[palpite]))
print("="*40)
if sorteio == lista[palpite]:
    print('EMPATE!!!')
elif sorteio == lista[0]:
    if lista[palpite] == lista[1]:
        print('Papel cobre pedra. \n você venceu!!!!')
    elif lista[palpite] == lista[2]:
        print('Pedra quebra tesoura. \n computador venceu!!!!')
elif sorteio == lista[1]:
    if lista[palpite] == lista[0]:
        print('Papel cobre pedra. \n computador venceu!!!')
    elif lista[palpite] == lista[2]:
        print('Tesoura corta papel. \n você venceu!!!')
elif sorteio == lista[2]:
    if lista[palpite] == lista[0]:
        print('Pedra quebra tesoura. \n você venceu!!!')
    elif lista[palpite] == lista[1]:
        print('tesoura corta papel. \n computador venceu!!!')
print('-='*10 , 'FIM', '-='*10)

#Desafio 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos 
# de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
for i in range (10, -1, -1):
    print(i)
    sleep(1)
print('FELIZ ANO NOVO!!!')

#Desafio 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo 
# entre 1 e 50.
for i in range(2,51, 2):
    print(i)

#Desafio 48:Faça um programa que calcule a soma entre todos os números que são múltiplos de três 
# e que se encontram no intervalo de 1 até 500.
soma = 0
for i in range(1,501,2 ):
     if i % 3 == 0:
          soma = soma + i
print(soma)

#Desafio 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, 
# só que agora utilizando um laço for.
numero = int(input('Digite um número para calcular a tabuada:'))
for i in range(0,11):
    print('{} x {} = {}'.format(numero, i, numero*i))

#Desafio 50: Desenvolva um programa que leia seis números inteiros 
# e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma  = 0
impares = []
for i in range(1 ,7):
  num = int(input('Digite um número: '))
  if num % 2 ==0:
    soma = soma + num
  elif num % 2 == 1:
    impares.append(i)
print('A soma dos números pares digitados é: {} \nOs números Impares foram {}'.format(soma, impares))

#Desafio 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.
print('='*20)
print('10 termos de uma PA')
print('='*20)
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
print(termo)
for i in range(0,9):
    termo = termo + razao
    print(termo)
print('ACABOU')

#Desafio 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um número: '))
tot = 0
for i in range(1, num + 1):
    if num % i == 0:
        tot += 1
if tot == 2:
    print('O núemro {} é primo'.format(num))
else:
    print('o número {} não é primo'.format(num))

#Desafio 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
# desconsiderando os espaços. Exemplos de palíndromos:
# PÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

# recebendo as frases, eliminando os espaços e separando os elementos
frase = input('Digite uma frase: ').upper()
lista_letras = [letra for letra in frase if letra != ' ']
lista_letras = ''.join(lista_letras)
#criando uma lista inversa para comparação
lista_inversa = lista_letras[::-1]
lista_inversa = ''.join(lista_inversa)
print('A frase {} inversa fica {}'.format(lista_letras, lista_inversa))
#comparando as duas listas
if lista_letras == lista_inversa:
    print('É um palindromo')
else:
    print('Não é um palindromo.')

#Desafio 54:Crie um programa que leia o ano de nascimento de sete pessoas.
#  No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import datetime
idade = []
maior = 0
menor = 0
for i in range(1,8):
    data=int(input('Digite o ano em que a {}ª pessoa nasceu: '.format(i)))
    idade.append(data)
for ano in idade:
    if datetime.now().year - ano >= 18:
        maior += 1
    else:
        menor += 1
print(' Ao todo temos {} pessoa maiores de idade \n e {} pessoas menores de idade'.format(maior, menor))
    
#Desafio 55: Faça um programa que leia o peso de cinco pessoas. 
# No final, mostre qual foi o maior e o menor peso lidos.
peso = []
for i in range(1,6): 
    valor = float(input('Digite o peso da {}ª pessoa: '.format(i)))
    peso.append(valor)
maior = max(peso)
menor = min(peso)
print('O maior peso lido foi {} e o menor foi {}'.format(maior, menor))

#Desafio 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, 
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
media_idade = 0
mais_velho = 0
mulheres = 0
for i in range(1,5):
    print('----{}ª pessoa----'.format(i))
    nome = input('Digite o nome da {}ª pessoa: '.format(i)).strip()
    idade = int(input('Digite a idade de {}: '.format(nome)))
    media_idade += idade
    sexo = input('Digite o sexo de {} (M/F): '.format(nome)).upper()
    if sexo == 'M' and idade > mais_velho:
        mais_velho = idade
        pessoa = nome
    if sexo == 'F' and idade < 20:
        mulheres =+ 1
print('A média de idade do grupo é de {:.0f} anos.'.format(media_idade/4))
print('O homem mais velho tem {} anos e se chama {}.'.format(mais_velho, pessoa))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulheres))

#Desafio 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = input('Digite seu sexo (M/F): ').strip().upper()[0]
while sexo not in 'MF':
    sexo = input('Dados inválidos, por favor, informe seu sexo (M/F): ').strip().upper()[0]    
print('Sexo {} registrado com sucesso!'.format(sexo))

'''Desafio 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
num = randint(0, 10)
tentativas = 0
print('-=-'*20)
print('Vou pensar em um número entre 0 e 10, tente adivinhar...')
print('-=-'*20)
palpite = int(input('Em qual número estou pensando?'))
tentativas += 1
while palpite != num:
    if palpite > num:
        print('Menos, tente mais uma vez')
        palpite = int(input('Qual o seu palpite? '))
        tentativas += 1
    if palpite < num:
        print('mais, tente mais uma vez')
        palpite = int(input('Qual o seu palpite? '))
        tentativas += 1
print('Acertou!!! com {} tentativas, o número escolhido foi {}'.format(tentativas, palpite))

'''Desafio 59: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
TEXTO = 'CALCULADORA'
print('=-='*20)
print(TEXTO.center(55))
print('=-='*20)
print('Digite os valores a serem calculados: ')
num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
menu = 0
while menu != 5:
    menu = int(input('''Escolha a operação a ser realizada:
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa  '''))
    if menu ==1:
        print('Você escolheu SOMAR:')
        print('Processando...')
        sleep(2)
        soma = num1 + num2
        print('A soma entre {} e {} é: {}'.format(num1, num2, soma))
        print('='*30)
        sleep(2)
    elif menu == 2:
        print('Você escolheu MULTIPLICAR: ')
        print('Processando...')
        sleep(2)
        multiplicacao = num1 * num2
        print(' A multiplicação entre {} e {} é: {}'.format(num1, num2, multiplicacao))
        print('='*30)
        sleep(2)
    elif menu == 3:
        print('Você escolheu COMPARAR: ')
        print('Processando...')
        sleep(2)
        maior = max(num1, num2)
        print('Entre {} e {}, o maior é {}'.format(num1, num2, maior))
        print('='*30)
        sleep(2)
    elif menu == 4:
        print('Você escolheu ALTERAR:')
        print('Quais os novos valores?')
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        print('Processando...')
        sleep(2)
        print('Atualizado!\nAgora os novos valores são: {} e {}.'.format(num1, num2))
        print('='*30)
        sleep(2)
        print('O que você deseja fazer agora?')
    elif menu == 5:
        print('finalizando... Estarei aqui quando precisar.')
        sleep(1)
    else:
        print('Opção inválida')
print('Fim do programa.')

'''Desafio 60: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120'''
print('Calculo de fatorial.')
numero = int(input("Digite um número: "))  
fatorial = 1  
contador = numero  
while contador > 1:  
    fatorial *= contador  
    contador -= 1  
print(f"O fatorial de {numero} é {fatorial}")

'''Desafio 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''
print('='*20)
print('10 termos de uma PA')
print('='*20)
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
print(termo)
while cont < 10:
    termo = termo + razao
    print(termo)
    cont += 1
print('ACABOU')

'''Desafio 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar
 mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.'''
print('='*20)
print('progressão aritmetica')
print('='*20)
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
print(termo, end=' ')
while cont < 10:
    termo = termo + razao
    print(termo, end=' ')
    cont += 1
print('Pausa')
contador = 1
while contador > 0:
    contador += 1
    cont2= int(input('\nQuantos termos você quer mostrar a mais? '))
    if cont2 == 0:
        contador =0
    while cont2 > 0:
        termo += razao
        print(termo, end =' ')
        cont2 -= 1
        cont += 1
    print('Pausa')
print('Progressão finalizada com {} termos mostrados'.format(cont))
print('=-'*20)

'''Desafio 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
Exemplo:
0 – 1 – 1 – 2 – 3 – 5 – 8'''
print('-'*25)
print('SEQUENCIA DE FIBONACCI')
print('-'*25)
termos = int(input('Quantos termos você quer mostrar? '))
f0 = 0
f1 = 1
fn = 2
print(f0, '>', f1, '>', end=' ')
termos -=2
while termos >0:
    fn = f0 + f1
    print(fn, '>', end=' ')
    f0 = f1 
    f1 = fn
    fn = (f0 -1) + (f1-2)
    termos -= 1
    
'''Desafio 64: Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''
cont = 0
num = 0
n = 0
n = int(input('Digite um núemro [999 para parar]: '))
while n != 999:
    num += n
    cont += 1
    n = int(input('Digite um núemro [999 para parar]: '))
print('Você digitou {} números e a soma deles foi: {}'.format(cont, num))
