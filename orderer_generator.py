# Exercises

# Increase the prices of the following products by 10%
# Generate new_products by deep copy (deep copy)
# Sort the products by descending name (from highest to lowest)
# Generate products_ordered_by_name by deep copy
# Sort products by increasing price (from lowest to highest)
# Generate products_ordered_by_price by deep copy


import copy 

products= [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


#step 1 - 10% increment

new_products_1=copy.deepcopy(products)

for index, new_item in enumerate(new_products_1):

    #print(index,new_item)
    for key,value in new_item.items():
        
        try:
            value=float(value)
            value=value+(value/10)
            new_item.update({key:round(value,4)})
            
        except:
            value=value

#for index, new_item in enumerate(new_products_1):
 #   for key,value in new_item.items():
  #      print(f'{key} - {value}')
    
#step 2 - Sort the products by descending name (from highest to lowest)

new_products_2=copy.deepcopy(new_products_1)

new_products_2 = sorted(new_products_2, key=lambda item: item['nome'], reverse=True)



#step 3 - Sort products by increasing price (from lowest to highest)

new_products_3=copy.deepcopy(new_products_2)
new_products_3 = sorted(new_products_2, key=lambda item: item['preco'])



print('Original List:',end='\n')
for item in products:
    print(item)
print('10% Increment List:',end='\n')
for item in new_products_1:
    print(item)
print('Sort by Name:',end='\n')
for item in new_products_2:
    print(item)
print('Sort by Price:',end='\n')
for item in new_products_3:
    print(item)
