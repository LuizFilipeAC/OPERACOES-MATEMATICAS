# ----- APRESENTAÇÃO -----
from seconde_degree.resolution import calculate_coefficient,  processing_data, calculating_equation

print('----------------------------------------------------------------------------------')
print('Nosso projeto visa entregar uma resolução para os seus problemas de matemática!')
print('----------------------------------------------------------------------------------')

while True:
    option = input('----- Selecione uma opção! -----\n'
                '[ 1 ] - Equação do segundo grau\n'
                '[ 2 ] - \n' 
                '[ x ] - Sair do programa\n'
                'OPÇÃO -> '
                    )

    if option == '1':
        a, b, c = calculate_coefficient()
        coefficients = processing_data(a, b, c)
        if coefficients is not None:
            a, b, c = processing_data(a, b, c)
        else:
            print('Você inseriu um dado incorreto!!')
            continue

        # --- descobrindo os valores para X ---
        calculating_equation(a, b, c)
        continue

    # ENCERRANDO O FUNCIONAMENTO
    if option == 'x':
        
        exit()
         
        


