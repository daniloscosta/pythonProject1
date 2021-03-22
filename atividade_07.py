
custo = float(input("Digite o valor da venda: "))
taxaImposto = int(input("Digite a taxa de imposto: "))
valorImposto = custo * (taxaImposto * 0.01)
somaImposto = custo + valorImposto
print ("Com uma taxa de {}%, o valor do imposto é de {:.2f} e o custo final da venda com o imposto será de {:.2f}.".format(taxaImposto, valorImposto, somaImposto))