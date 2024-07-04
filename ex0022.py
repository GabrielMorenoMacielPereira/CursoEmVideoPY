nome=str(input('Qual o seu nome completo: ')).strip()
print(f'O seu nome com todas as letras maiusculas é {nome.upper()}')
print(f'O seu nome com todas as letras minusculas é {nome.lower()}')
print(f'O seu nome possui {len(nome)- nome.count(" ")} letras')
print(f'O seu primeiro nome possui {nome.find(" ")} letras')
#Outra forma de fazer a contagem de letras do primeiro nome
#separa = nome.split()
#print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')
