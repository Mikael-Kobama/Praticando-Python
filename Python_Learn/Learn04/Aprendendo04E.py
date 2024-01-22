nome=str(input('Digite Seu nome: ')).strip()
nome.upper()
silva=nome.find('SILVA')
if silva==-1:
    silva='Não possui'
else:
    silva='Possui'
nome.capitalize()
separa=nome.split()


print(('A Pessoa {} {} {} ''Silva'' no Nome'.format(separa[0], separa[1], silva)))