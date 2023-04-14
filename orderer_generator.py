# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)


import copy 

products= [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]



def show_list(show_products):
    for item in show_products:
        print(item)

#show_list(products)

new_products_1=copy.deepcopy(products)

for index, new_item in enumerate(new_products_1):

    #print(index,new_item)
    for key,value in new_item.items():
        
        try:
            value=float(value)
            value=value+(value/10)
            new_item.update({key:value})
            
        except:
            value=value

for index, new_item in enumerate(new_products_1):
    for key,value in new_item.items():
        print(f'{key} - {value}')
    

new_products_2=copy.deepcopy(new_products_1)

new_products_2 = sorted(new_products_2, key=lambda item: item['nome'])

print(new_products_2)


new_products_3=copy.deepcopy(new_products_2)
new_products_3 = sorted(new_products_2, key=lambda item: item['preco'])

print(new_products_3)