#1 variável peso
Peso = float(input("Digite o peso total dos peixes: "))
#2 variável diferença do peso, para podermos fazer regra de 3 e conseguir calcular a multa
Peso_Diferenca = Peso - 50
#3 - Variável multa, excesso do peso x 4
Multa = Peso_Diferenca * 4
#4 Condição IF/ELSE, se passar o valor limite, mostrar o valor da multa e quantidade.
if Peso > 50:
    print('O peso para não ser multado foi ultrapassado, o valor da multa é', Multa, 'R$, O peso foi ultrapassado em', Peso_Diferenca, 'KG')
else:
    print('O peso esta na media para nao ser taxado')
#Teste executado com sucesso