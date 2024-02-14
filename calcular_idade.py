import random
import string
from datetime import datetime

nome = input('Digite seu nome: ')
print('Olá, {}!'.format(nome))

def calcular_idade(data_de_nascimento):
    data_atual = datetime.now()
    ano_nascimento = int(data_de_nascimento.split('/')[2])
    mes_nascimento = int(data_de_nascimento.split('/')[1])
    dia_nascimento = int(data_de_nascimento.split('/')[0])

    idade = data_atual.year - (ano_nascimento) - ((data_atual.month, data_atual.day) < (mes_nascimento, dia_nascimento))
    return idade

def main():
    try:
        dia_nascimento = int(input('Digite o dia em que nasceu: '))
        mes_nascimento = int(input(' Digite o mês em que nasceu: '))
        ano_nascimento = int(input('Digite o ano em que nasceu: '))
        
        data_de_nascimento = '{}/{}/{}'.format(dia_nascimento, mes_nascimento, ano_nascimento)
        idade = calcular_idade(data_de_nascimento)
        print('{} Sua idade é: {} anos.'.format(nome, idade))
        

    except ValueError:
        print('Formato de data incorreto. Certifique-se de usar o formato (DD/MM/AAAA).')



if __name__ == '__main__':
        main()