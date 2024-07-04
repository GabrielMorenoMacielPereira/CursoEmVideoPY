frase=str(input('Digite uma frase qualquer: ')).lower().strip()
print(f'A letra A aparece {(frase.count("a"))} vezes')
print(f'A primeira letra A aparece na posição {frase.find("a", "á", "ã", "à")}')
print(f'A última letra A aparece na posição {frase.rfind("a")}')


