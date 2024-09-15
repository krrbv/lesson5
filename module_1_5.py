immutable_var = 1, 2, True, "cake"
print(immutable_var)
immutable_var_1 = (1, 2, True, "cake")
print(immutable_var_1)
immutable_var_2 = tuple([1, 2, True, "cake"])
print(immutable_var_2)

#immutable_var[0] = 3
#print(immutable_var) - ошибка. Кортеж - неизменяемый тип данных. Кортеж не поддерживает обращение по элементам.
#однако, кортеж может хранить какие-то изменяемые объекты. создам кортеж, внутри которого будет список, и изменю элемент этого внутреннего списка
immutable_var = (1, 2, [3, 4], True, "cake")
immutable_var[2][0] = 6
print(immutable_var)

mutable_list = [5, "School", False, "banana", 7]
mutable_list[0] = 7
mutable_list[3] = "apple"
mutable_list.append("lesson")
mutable_list.extend("sunday")
mutable_list.extend(["winter", 10])
print(mutable_list)
