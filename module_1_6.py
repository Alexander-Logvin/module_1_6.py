my_dict = {'Alex': 1995, 'Alena': 1997, 'Artem': 2021, 'Matvei': 2023 }
print(my_dict)
print(my_dict.get('Alex'))
print(my_dict.get('Anton'))
my_dict.update({'Denis': 1995, 'Artur': 1986})
my_dict.pop('Denis')
print(my_dict.get('Denis'))
print(my_dict)
my_set = {1, 2 , 3, 4, 5, 'Alex', 1, 2, 2, 5}
print(my_set)
print(my_set.add(6))
print(my_set.add('Artem')) #Выдает ошибку при добавлении сразу два значения во множество. По этому сделал двумя командами.
print(my_set)
print(my_set.discard(3))
print(my_set)