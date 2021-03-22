#Recebe as notas e calcula a media
a = int(input('Primeiro bimestre: '))
if a > 10:
    a = int(input('Você digitou errado. \nDigite novamente o primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
if b > 10:
    b = int(input('Você digitou errado. \nDigite novamente o segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
if c > 10:
    c = int(input('Você digitou errado. \nDigite novamente o terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
if d > 10:
    d = int(input('Você digitou errado. \nDigite novamente o quarto bimestre: '))
media = (a + b + c + d) / 4
print('media: {}'.format(media))
if media > 6:
     print('Aluno aprovado!')
else:
     print('Aluno reprovado!')

# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('media: {}'.format(media))
# else:
#     print('Foi digitado algum valor errado :(')
#     exit(0)
#
# if media > 6:
#     print('Aluno aprovado!')
# else:
#     print('Aluno reprovado!')





#'Verifica se os dois números e diz se tem algum par'
# a = int(input('Digite o primeiro número: '))
# b = int(input('Digite o segundo número: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or not resto_b > 0:
#     print('Foi digitado um número par!')
# else:
#     print('Nenhum número par foi digitado!')

# 'Recebe três valores e mostra qual e o maior'
# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
# if a > b and a > c:
#     print('O maior número é {}'.format(a))
# elif b > a and b > c:
#     print('O maior número é {}'.format(b))
# else:
#     print('O maior número é {}'.format(c))
# print('Final do programa!')
