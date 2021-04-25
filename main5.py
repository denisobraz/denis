fruit = ('apple', 'pear', 'cherry', 'banana', 12)
vegetables = ('tomato', 'onion', 'carrot', 17)
berries = ('blueberry', 'cranberry', 'watermelon', 8)
new_fruit = []
for i in fruit[0:4]:
    new_fruit.append(i.title())
    print(new_fruit)

new_vegetables = []
for i in vegetables[0:3]:
    new_vegetables.append(i.title())
    print(new_vegetables)

new_berries = []
for i in berries[0:3]:
    new_berries.append(i.title())
    print(new_berries)

    #4

new_fruit = list(new_fruit)
new_fruit = []
for i in new_fruit:
    i = i[0:6]
    new_fruit.append(i)
    print(fix_fruit)
