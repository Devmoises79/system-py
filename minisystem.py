



print('Olá, qual é o seu nome?')

nome = input()

print('Olá ' + nome + ', quantos anos você tem?')

idade = input()

print('Olá ' + nome + ', você tem ' + idade + ' anos.')


if int(idade) >= 18:
    print('Você é maior de idade. Usuário autorizado.')
else:
    print('Você é menor de idade. Acesso negado.')
