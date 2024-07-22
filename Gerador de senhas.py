import random

print("Este é um gerador de senhas fortes! >:)")

caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@!$%#'

número = input('Quantidade de senhas a ser geradas: ')
número = int(número)

tamanho = input('Insira o tamanho de sua senha: ')
tamanho = int(tamanho)

print('\nAqui estão suas senhas :) : ')

for senhas in range(número):
    senhas = ''
    for c in range (tamanho):
        senhas += random.choice(caracteres)
    print(senhas)    