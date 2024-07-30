def BoasVindas():
    print('\nBem vindo a Calculadora Python Refatorada!\n')
    print('Calculadora Python Version 1.1\n')



def adicao(primeiro_valor, segundo_valor):
    return primeiro_valor + segundo_valor

def subtracao(primeiro_valor, segundo_valor):
    return primeiro_valor - segundo_valor

def multiplicacao(primeiro_valor, segundo_valor):
    return primeiro_valor * segundo_valor

def divisao(primeiro_valor, segundo_valor):
    
    if segundo_valor == 0:
        print('Não foi possível realizar a divisão por 0')
        return None
    else:
        return primeiro_valor / segundo_valor
    
    
def calculadora(primeiro_valor, segundo_valor, operacao):

    if operacao == '+' or operacao == 'adição':
       return adicao(primeiro_valor, segundo_valor)
    elif operacao == '-' or operacao == 'subtração':
        return subtracao(primeiro_valor, segundo_valor)
    elif operacao == '*' or operacao == 'multiplicação':
       return multiplicacao(primeiro_valor, segundo_valor)
    elif operacao == '/' or operacao == 'divisão':
        return divisao(primeiro_valor, segundo_valor)
    else:
        print('Operação inválida')
        return None

    

saida = ''

while saida.lower() != 'n':

    BoasVindas()

    primeiro_valor = float(input('Digite o Primeiro valor: \n'))

    operacao = input('\nDigite a operação desejada (+, -, *, /), ou seu nome: \n')

    segundo_valor = float(input('\nDigite o Segundo valor: \n'))

    resultado = calculadora(primeiro_valor, segundo_valor, operacao)

    print(f'\nResultado da operação: {primeiro_valor} {operacao} {segundo_valor} = {resultado}\n')

    saida = input('Deseja continuar? (s/n): ')


print('Programa encerrado')









    