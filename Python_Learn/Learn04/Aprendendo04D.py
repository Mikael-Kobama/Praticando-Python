cidade=str(input('DIgite o nome da Cidade: ')).strip()
cidade.upper()
santo= cidade.find('SANTO')
if santo==-1:
    santo='Não'
else:
    santo='Sim'
print('A Cidade {} possui santo no começo? \n'
      'R: {}'.format(cidade, santo))