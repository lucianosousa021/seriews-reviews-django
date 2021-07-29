
def nota_inteiro(nota, errors_list):
    """ verifica se a nota é inteira e está entre 0 e 10"""
    if 0 <= nota <= 10:
        pass
    else:
        errors_list['serie_rating'] = 'A nota deve ser um valor inteiro entre 0 e 10.'

def campo_vazio(valor, errors_list, campo):
    """ verifica se um campo está vazio"""
    print(valor, campo)
    if valor == "":
        errors_list[campo] = 'Este campo deve ser preenchido.'