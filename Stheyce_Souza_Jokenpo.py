from time import sleep
rodadas = ['Rodada n1', 'Rodada n2', 'Rodada n3']
pp = 0
p = 0
print('''Bem vindo ao JokenPo.
intruções:
'1' para Pedra
'2' para Papel
'3' para Tesoura''')
nome = input('Login: ')
nome2 = input('Login: ')
print('=' * 80)

for n in rodadas:
    print(n)
    ppt = input('Pedra, Papel, Tesoura...').strip()
    if ppt == '1' or ppt == '2' or ppt == '3':
        if ppt == '1':
             print(f'{nome}: Pedra')
        elif ppt == '2':
             print(f'{nome}: Papel')
        elif ppt == '3':
              print(f'{nome}: Tesoura')
        sleep(0.75)
        
    pptt = input('Pedra, Papel, Tesoura...').strip()
    if pptt == '1' or pptt == '2' or pptt == '3':
        if pptt == '1':
             print(f'{nome2}: Pedra')
        elif pptt == '2':
             print(f'{nome2}: Papel')
        elif pptt == '3':
              print(f'{nome2}: Tesoura')
        sleep(0.75)
        
        if ppt == str(pptt):
            print('Juiz: Ops, foi empate!')
        elif (ppt == '1' and pptt == '2')or (ppt == '2' and pptt == '3')or (ppt == '3' and pptt == '1'):
            print('juiz: Parabéns ! jogador Nº2 venceu !')
            pp = pp+1
        else:
            print('juiz: Parabéns ! jogador Nº1 venceu !')
            p = p+1
    else:
        print('Erro;Escolha inválida !')

    if p == 2 and pp == 0:
        print ('Jogo encerrado, jogador nº1 venceu')

    if pp == 2 and p == 0:
        print ('Jogo encerrado, jogador nº2 venceu')

print('----------------------------------')
if p>pp:
    print( 'ganhador:',nome)
    print('pontos:',p)

if pp>p:
    print(' ganhador:',nome2)
    print('pontos:',pp)
print('----------------------------------')