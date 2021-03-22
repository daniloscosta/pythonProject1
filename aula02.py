a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
print(type(a))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
restoDiv = a % b
resultado = ('A Soma é {soma}.'
      '\nA Subtração é {sub}. '
      '\nA Divisão é {div}.'
      '\nA Multiplicação é {multi}.'
      '\nO Resto da divisão é {resto}.'
                           .format(soma=soma,
                                   div=divisao,
                                   multi=multiplicacao,
                                   sub=subtracao,
                                   resto=restoDiv))

print(resultado)