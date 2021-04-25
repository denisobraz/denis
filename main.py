fruit = ('apple', 'pear', 'cherry', 'banana', 12)
vegetables = ['tomato', 'onion', 'carrot', 17]
berries = ('blueberry', 'cranberry', 'watermelon', 8)
basket = {}
basket ['fruit'] = fruit
basket['vegetables'] = vegetables
basket['berries'] = berries

print(basket)

#3
basket['finished'] = ('Carrot', 'Watermelon')
basket.update({'vegetables': ('tomato', 'onion', 'cabbage', 17 )})
basket.update({'barries':('blueberry', 'cranberry', 'cherry', 8)})
print(basket)
