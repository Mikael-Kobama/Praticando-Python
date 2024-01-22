nome=str(input('Digite Seu Nome Completo: ')).strip()
min=nome.lower()
mai=nome.upper()
separa=nome.split()

print('Seu Nome é {} \n'
      'Em minusculo é {} \n'
      'Em Maiusculo é {} \n'
      'Ao todo possui {} Letras \n'
 #     'Seu Primeiro Nome possui {} letras'.
      'Seu primeiro nome é {} e Possui {} Letras '.format(nome, min,mai,len(nome)-nome.count(' '), separa[0], len(separa[0]) ))