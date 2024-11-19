immutable_var = ([1, 3], 1, 2, 3, 'Олег', False)
# immutable_var[4] = 'Данил'
# immutable_var[5] = True
# immutable_var[4][-1] = 'п'
immutable_var[0][0] = 4 # В отличии от списка, в кортеже объекты неизменяемы, элименты можно изменить только внутри элемента типа list
print(immutable_var)
print(end='\n')
mutable_list = [[5, 6], 3, 5, 8, 'Полина', True]
mutable_list[ : ] = [[3, 4], 2, 4, 5, 'Аркадий', False]
print(mutable_list)