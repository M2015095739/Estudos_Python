print('1 - Windows Server')
print('2 - Unix')
print('3 - Linux')
print('4 - Netware')
print('5 - Mac Os')
print('6 - Outro')

voto = int(input(
    print('Na sua opinião qual o melhor sistema operacional para uso de servidores?Escolha uma das opções acima: ')))

votacao = [0, 0, 0, 0, 0, 0] 
candidatos = ['Windows Server' , 'Unix', 'Linux' , 'Netware', 'Mac Os' , 'Outro']
voto_w = 0
voto_u = 0
voto_l = 0
voto_n = 0
voto_m = 0
voto_o = 0

while voto != 0: 

    while voto > 6 :
        voto = int(input(print('Número inválido, digite novamente: ')))

    if voto == 1:
        voto_w = voto_w + 1
        votacao[0] = voto_w
    elif voto == 2:
        voto_u = voto_u + 1
        votacao[1] = voto_u
    elif voto == 3:
        voto_l = voto_l + 1
        votacao[2] = voto_l
    elif voto == 4:
        voto_n = voto_n + 1
        votacao[3] = voto_n
    elif voto == 5:
        voto_m = voto_m + 1
        votacao[4] = voto_m
    elif voto == 6:
        voto_o = voto_o + 1
        votacao[5] = voto_o
    
    voto = int(input(print('Na sua opinião qual o melhor sistema operacional para uso de servidores? ')))
    total_votos = sum(votacao)  

print('Fim de votação !!!')
print('-------------------------------------------------------------')
print('Sistema Operacional    Votos                    %')
print('-------------------------------------------------------------')
print('Windows Server', '         ', votacao[0], '        ', votacao[0] / total_votos * 100)
print('Unix', '                   ', votacao[1], '        ', votacao[1] / total_votos * 100)
print('Linux', '                  ', votacao[2], '        ', votacao[2] / total_votos * 100)
print('Netware', '                ', votacao[3], '        ', votacao[3] / total_votos * 100)
print('Mac Os', '                 ', votacao[4], '        ', votacao[4] / total_votos * 100)
print('Outro', '                  ', votacao[5], '        ', votacao[5] / total_votos * 100)
print('--------------------------------------------------------------')
print('Total de votos válidos: ', total_votos)



#print('O sistema operacional vencedor foi: ')


