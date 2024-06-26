# COLETANDO OS VALORES DOS COEFICIENTES

def calculate_coefficient():
    a = input('Insira o valor do coeficiente A: ')
    b = input('Insira o valor do coeficiente B: ')
    c = input('Insira o valor do coeficiente C: ')
    return a, b, c

def processing_data(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        return a, b, c
    except ValueError:
        return None
        
# PEGANDO OS COEFICIENTES, JÁ DEPOIS DA ANÁLISE, E EFETUANDO O CALCULO
def calculating_equation(a, b, c):
    # BHASKARA
    delta = (b**2) - (4 * a * c)
    raiz_quadrada = delta ** 0.5
    
    if delta == 0:
        x = -b / (2 * a)
        print(x)
    elif delta > 0:
        x1 = (-b + raiz_quadrada) / (2 * a)
        x2 = (-b - raiz_quadrada) / (2 * a)
        print(x1, x2)
    elif delta < 0:
        print('NÃO HÁ SOLUÇÃO')