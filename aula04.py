
for i in range(101):
    div = 0
    for x in range(1, i):
        resto = i % x
        if resto == 0:
            div += 1
    if div == 2:
         print('O número {} é primo!'.format(i))







1






#
# num = int(input('Digite um número: '))
#
# div = 0
# for x in range(1, num+1):
#     resto = num % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#      print('O número {} é primo!'.format(num))
# else:
#      print('O número {} não é primo!'.format(num))