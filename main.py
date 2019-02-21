mathScores = [60, 70, 10, 20, 81, 63, 1521]
print(sum(mathScores))
print(max(mathScores))
s = sum(mathScores)
l = len(mathScores)
print(s/l)
mathScores.append(63)
del mathScores[0:2]
print(mathScores)
mathScores[2] = 100
print(mathScores)
print(100 in mathScores)
ls = [[1, 2, 3],[4, 5, 6]]
print(ls[0][0])
print(sorted(mathScores))
print('-----------------------------------')

tuple1 = (1, 2, 3, 4, 5)
tuple2 = '1', '2', '3', '5929185', '5'
print(sorted(tuple1))
print(tuple2.index('5929185'))
tuple3 = ('Lisa', 23, 'Female')
name, age, sex = tuple3
print(name, age, sex)
print(tuple3[0:2])
tuple4 = ('a', 'b')
print(tuple1+tuple4)
print('-----------------------------------')

family = {'dad':'Homer', 'mom':'Marge', 'son':'Bart', 'daughter':'Lisa'}
print(family['dad'])
print(family.get('dad'))
print('dad' in family)
print('Homer' in family)
print(family.keys())
print(family.values())
print(family.items())
family['cousin'] = 'weihan'
family.update({'uncle':'Martin', 'aunt':'May'})
print(family.pop('son'))
del family['daughter']
family['cousin'] = 'weihan weihan'
print(family)
print(family.get('son'))
print('-----------------------------------')

fruit = {'apple', 'banana', 'guava', 'guava'}
print(fruit)
fruit1 = {'strawberry', 'papaya', 'banana'}
print(fruit | fruit1)
print(fruit & fruit1)
print(fruit - fruit1)
fruit.add('watermelon')
print(fruit)
