""" Aula 03 - Args e Kwargs em funções e métodos """

# Definição da função de títulos da copa do mundo por país
def world_cup_titles(country, *args):
    print('Country: ', country)
    for title in args:
        print('year: ', title)

# Chamada com 5 itens no *args:
world_cup_titles('Brasil', '1958', '1962', '1970', '1994', '2002')

# Chamada com 1 item no *args:
world_cup_titles('Espanha', '2010')


# Definição da função de cálculo de preço
def calculate_price(value, **kwargs):
    tax_percentage = kwargs.get('tax_percentage')
    discount = kwargs.get('discount')

    if tax_percentage:
        value += value * (tax_percentage / 100)
    if discount:
        value -= discount
    
    return value

# Chamada sem kwargs:
final_price = calculate_price(100.0)
print(final_price)

# Chamada com o kwarg discount:
final_price = calculate_price(100.0, discount=5.0)
print(final_price)

# Chamada com o kwarg tax_percentage:
final_price = calculate_price(100.0, tax_percentage=7)
print(final_price)

# Chamada com os kwargs discount e tax_percentage:
final_price = calculate_price(100.0, tax_percentage=7, discount=5.0)
print(final_price)
