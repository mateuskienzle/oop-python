from pessoa import proprietario
from modelos import bmw, celta, chevete, ferrari, focus, gol, lambo, mercedes, palio, porsche
from time import sleep

print('=-' * 17)
print('Essa é a concessionária dos guri!')
print('=-' * 17)
sleep(2)

print('Informe abaixo, de acordo com as opções, o que você procura')
print('[1] Quero alugar um carro')
print('[2] Quero comprar um carro')
print('[3] Estou apenas dando uma olhada')
sleep(3)
escolha = int(input('Informe a sua opção (1, 2 ou 3): '))
print('-' * 20)
if escolha == 1:
    print('Entendido! Aqui temos as opções de locação disponíveis para hoje: ')
    sleep(2)
    print('[1] - Gol ano 98')
    print('[2] - Celta ano 2001')
    print('[3] - Palio ano 2005')
    print('[4] - Chevete ano 90')
    print('[5] - Focus ano 2012')

    escolha_aluga = int(input('Você tem interesse em qual dos nossos modelos (1, 2, 3, 4 ou 5)? '))
    if escolha_aluga == 1:
        sleep(2)
        print('-' *20)
        print('Perfeito! Aqui estão algumas informações do veículo: ')

        c1 = gol(
            modelo = 'Gol',
            cor = 'Branco',
            placa = 'XXX-9999',
            ano = '1998',
            kilometragem = '205 mil Km'
        )

        print(c1.__dict__)
        print('-' * 20)
        print('Agora, preciso dos seus dados para registrarmos na ficha:')

        proprietario_c1 = proprietario(
            nome = str(input('Qual seu nome? ')),
            idade = int(input('Qual sua idade? ')),
            cpf = input('Qual seu CPF? '),
            endereco = input('Qual seu endereço? ')
        )
        
        print('Legal, aqui está a ficha do veículo \n',c1.__dict__, '\nE aqui está a ficha com os seus dados: \n',proprietario_c1.__dict__)

        print('-' * 20)
        c1.ronco_motor()
        sleep(2)
        print('-' * 20)
        print('Obrigado pela preferência, até a próxima!')

    elif escolha_aluga == 2:
        sleep(2)
        print('-' *20)
        print('Perfeito! Aqui estão algumas informações do veículo: ')

        c2 = celta(
            modelo = 'Celta',
            cor = 'Prata',
            placa = 'XYX-9999',
            ano = '2001',
            kilometragem = '140 mil Km'
        )

        print(c2.__dict__)
        print('-' * 20)
        print('Agora, preciso dos seus dados para registrarmos na ficha:')

        proprietario_c2 = proprietario(
            nome = str(input('Qual seu nome? ')),
            idade = int(input('Qual sua idade? ')),
            cpf = input('Qual seu CPF? '),
            endereco = input('Qual seu endereço? ')
        )
        
        print('Legal, aqui está a ficha do veículo \n',c2.__dict__, '\nE aqui está a ficha com os seus dados: \n',proprietario_c2.__dict__)

        print('-' * 20)
        c1.ronco_motor()
        sleep(2)
        print('-' * 20)
        print('Obrigado pela preferência, até a próxima!')
    
    elif escolha_aluga == 3:
        sleep(2)
        print('-' *20)
        print('Perfeito! Aqui estão algumas informações do veículo: ')

        c3 = palio(
            modelo = 'Palio',
            cor = 'Azul marinho',
            placa = 'XYY-9999',
            ano = '2005',
            kilometragem = '100 mil Km'
        )

        print(c3.__dict__)
        print('-' * 20)
        print('Agora, preciso dos seus dados para registrarmos na ficha:')

        proprietario_c3 = proprietario(
            nome = str(input('Qual seu nome? ')),
            idade = int(input('Qual sua idade? ')),
            cpf = input('Qual seu CPF? '),
            endereco = input('Qual seu endereço? ')
        )
        
        print('Legal, aqui está a ficha do veículo \n',c3.__dict__, '\nE aqui está a ficha com os seus dados: \n',proprietario_c3.__dict__)

        print('-' * 20)
        c3.ronco_motor()
        sleep(2)
        print('-' * 20)
        print('Obrigado pela preferência, até a próxima!')

    elif escolha_aluga == 4:
        sleep(2)
        print('-' *20)
        print('Perfeito! Aqui estão algumas informações do veículo: ')

        c4 = chevete(
            modelo = 'Chevete',
            cor = 'Amarelo',
            placa = 'YYY-9999',
            ano = '1990',
            kilometragem = '290 mil Km'
        )

        print(c4.__dict__)
        print('-' * 20)
        print('Agora, preciso dos seus dados para registrarmos na ficha:')

        proprietario_c4 = proprietario(
            nome = str(input('Qual seu nome? ')),
            idade = int(input('Qual sua idade? ')),
            cpf = input('Qual seu CPF? '),
            endereco = input('Qual seu endereço? ')
        )
        
        print('Legal, aqui está a ficha do veículo \n',c4.__dict__, '\nE aqui está a ficha com os seus dados: \n',proprietario_c4.__dict__)

        print('-' * 20)
        c4.ronco_motor()
        sleep(2)
        print('-' * 20)
        print('Obrigado pela preferência, até a próxima!')

    elif escolha_aluga == 5:
        sleep(2)
        print('-' *20)
        print('Perfeito! Aqui estão algumas informações do veículo: ')

        c5 = focus(
            modelo = 'Focus',
            cor = 'Verde',
            placa = 'XYX-9999',
            ano = '2012',
            kilometragem = '180 mil Km'
        )

        print(c5.__dict__)
        print('-' * 20)
        print('Agora, preciso dos seus dados para registrarmos na ficha:')

        proprietario_c5 = proprietario(
            nome = str(input('Qual seu nome? ')),
            idade = int(input('Qual sua idade? ')),
            cpf = input('Qual seu CPF? '),
            endereco = input('Qual seu endereço? ')
        )
        
        print('Legal, aqui está a ficha do veículo \n',c5.__dict__, '\nE aqui está a ficha com os seus dados: \n',proprietario_c5.__dict__)

        print('-' * 20)
        c5.ronco_motor()
        sleep(2)
        print('-' * 20)
        print('Obrigado pela preferência, até a próxima!')

elif escolha == 2:
    print('Certo! Aqui temos as opções de venda disponíveis para hoje: ')
    sleep(2)
    print('[1] - Lamborghini')
    print('[2] - Porsche')
    print('[3] - BMW')
    print('[4] - Mercedes')
    print('[5] - Ferrari')     

    escolha_venda = int(input('Você tem interesse em qual dos nossos modelos (1, 2, 3, 4 ou 5)? '))
    if escolha_venda == 1:
        sleep(2)
        print('-' *20)
        print('Perfeito! Aqui estão algumas informações do veículo: ')

        c6 = lambo(
            modelo = 'Lamborghini',
            cor = 'Amarelo',
            placa = 'YYY-9999',
            ano = '2021',
            kilometragem = '0 Km'
        )

        print(c6.__dict__)
        print('-' * 20)
        print('Agora, preciso dos seus dados para registrarmos na ficha:')

        proprietario_c6 = proprietario(
            nome = str(input('Qual seu nome? ')),
            idade = int(input('Qual sua idade? ')),
            cpf = input('Qual seu CPF? '),
            endereco = input('Qual seu endereço? ')
        )
        
        print('Legal, aqui está a ficha do veículo \n',c6.__dict__, '\nE aqui está a ficha com os seus dados: \n',proprietario_c6.__dict__)

        print('-' * 20)
        c6.ronco_motor()
        sleep(2)
        print('-' * 20)
        print('Obrigado pela preferência, até a próxima!')
        
    if escolha_venda == 2:
        sleep(2)
        print('-' *20)
        print('Perfeito! Aqui estão algumas informações do veículo: ')

        c7 = porsche(
            modelo = 'Porsche',
            cor = 'Preto',
            placa = 'YXX-9999',
            ano = '2020',
            kilometragem = '300 Km'
        )

        print(c7.__dict__)
        print('-' * 20)
        print('Agora, preciso dos seus dados para registrarmos na ficha:')

        proprietario_c7 = proprietario(
            nome = str(input('Qual seu nome? ')),
            idade = int(input('Qual sua idade? ')),
            cpf = input('Qual seu CPF? '),
            endereco = input('Qual seu endereço? ')
        )
        
        print('Legal, aqui está a ficha do veículo \n',c7.__dict__, '\nE aqui está a ficha com os seus dados: \n',proprietario_c7.__dict__)

        print('-' * 20)
        c7.ronco_motor()
        sleep(2)
        print('-' * 20)
        print('Obrigado pela preferência, até a próxima!')

    if escolha_venda == 3:
        sleep(2)
        print('-' *20)
        print('Perfeito! Aqui estão algumas informações do veículo: ')

        c8 = bmw(
            modelo = 'BMW',
            cor = 'Branco',
            placa = 'YYX-9999',
            ano = '2020',
            kilometragem = '380 Km'
        )

        print(c8.__dict__)
        print('-' * 20)
        print('Agora, preciso dos seus dados para registrarmos na ficha:')

        proprietario_c8 = proprietario(
            nome = str(input('Qual seu nome? ')),
            idade = int(input('Qual sua idade? ')),
            cpf = input('Qual seu CPF? '),
            endereco = input('Qual seu endereço? ')
        )
        
        print('Legal, aqui está a ficha do veículo \n',c8.__dict__, '\nE aqui está a ficha com os seus dados: \n',proprietario_c8.__dict__)

        print('-' * 20)
        c8.ronco_motor()
        sleep(2)
        print('-' * 20)
        print('Obrigado pela preferência, até a próxima!')

    if escolha_venda == 4:
        sleep(2)
        print('-' *20)
        print('Perfeito! Aqui estão algumas informações do veículo: ')

        c9 = mercedes(
            modelo = 'Mercedes',
            cor = 'Branco',
            placa = 'YXY-9999',
            ano = '2018',
            kilometragem = '1080 Km'
        )

        print(c9.__dict__)
        print('-' * 20)
        print('Agora, preciso dos seus dados para registrarmos na ficha:')

        proprietario_c9 = proprietario(
            nome = str(input('Qual seu nome? ')),
            idade = int(input('Qual sua idade? ')),
            cpf = input('Qual seu CPF? '),
            endereco = input('Qual seu endereço? ')
        )
        
        print('Legal, aqui está a ficha do veículo \n',c9.__dict__, '\nE aqui está a ficha com os seus dados: \n',proprietario_c9.__dict__)

        print('-' * 20)
        c9.ronco_motor()
        sleep(2)
        print('-' * 20)
        print('Obrigado pela preferência, até a próxima!')

    if escolha_venda == 5:
        sleep(2)
        print('-' *20)
        print('Perfeito! Aqui estão algumas informações do veículo: ')

        c10 = ferrari(
            modelo = 'Ferrari',
            cor = 'Vermelho',
            placa = 'YYX-9999',
            ano = '2019',
            kilometragem = '910 Km'
        )

        print(c10.__dict__)
        print('-' * 20)
        print('Agora, preciso dos seus dados para registrarmos na ficha:')

        proprietario_c10 = proprietario(
            nome = str(input('Qual seu nome? ')),
            idade = int(input('Qual sua idade? ')),
            cpf = input('Qual seu CPF? '),
            endereco = input('Qual seu endereço? ')
        )
        
        print('Legal, aqui está a ficha do veículo \n',c10.__dict__, '\nE aqui está a ficha com os seus dados: \n',proprietario_c10.__dict__)

        print('-' * 20)
        c10.ronco_motor()
        sleep(2)
        print('-' * 20)
        print('Obrigado pela preferência, até a próxima!')

elif escolha == 3:
    print('Claro! Fique à vontade para conferir nossos modelos de veículos')