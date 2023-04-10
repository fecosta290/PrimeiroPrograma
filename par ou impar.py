from random import randint
n = r = c = 0
pc = randint(0, 10)
opcao = ''
print('-'*40)
print('       VAMOS JOGAR PAR OU IMPAR      ')
print('-'*40)
while True:
    n = int(input('digite um valor[0/10]:'))
    opcao = str(input('Par ou Impar[P/I]:')).upper() .strip()[0]
    print('-' * 40)
    print(f'o computador jogou {pc}')
    r = n + pc
    if r % 2 == 0 and opcao in'Pp':
        print('-' * 40)
        print(f'você jogou {n} e o computador {pc}, o resultado foi {r}. Deu PAR')
        print('você venceu')
        print('vamos continuar jogando...')

    if r % 2 == 1 and opcao in'Ii':
        print(f'você jogou {n} e o computador {pc}, o resultado foi {r}. Deu impar')
        print('você venceu')
        print('vamos continuar jogando...')

    if r % 2 == 0 and opcao in'Ii' or r % 2 == 1 and opcao in'Pp' :
        break
    c += 1


print(f'você jogou {n} e o computador {pc}, o resultado foi {r}.')
print('voê perdeu')
print('até a proxima...')
print('-'*20)
print(f'GAME-OVER, você ganhou {c} vezes \naté a proxima')
