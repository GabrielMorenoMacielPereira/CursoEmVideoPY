print('Vamos descobrir o valor a ser pago pelo aluguel do carro!')
dias=float(input('Qual a quantidade de dias pelos quais o carro foi alugado?'))
km=float(input('Qual a quantidade de km percorridos durante o período de aluguel?'))
print(f'O valor a ser pago pelo aluguel do carro é R${km*0.15+dias*60:.2f}')