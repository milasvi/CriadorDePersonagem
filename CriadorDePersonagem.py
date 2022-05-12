print('Bem-vinde ao Criador de Personagem! Escolha as características do seu personagem: \n')
contador = 0
contador1 = 0
contador2 = 0
contador3= 0


while True:
    classe = input('Escolha a classe do personagem: \n[1]Arqueire \n[2]Mage \n[3]Guerreire')
    idade = int(input('Escolha a idade: '))
    outro =input('Deseja criar outro personagem?[S/N]')
    if idade > 17:
        contador = contador + 1
    if classe == '1':
        contador1 = contador1 + 1
    if classe == '2':
        contador2 = contador2 + 1
    if classe == '3':
        contador3 = contador3 + 1

    if outro == 'N':
        print(f'Você criou {contador} adultos, {contador1} arqueires, {contador2} mages e {contador3} guerreires.')
        break
    