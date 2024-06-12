Immutable_var = 1, 2, 3, 'apple', False, "string"
print('Immutable tuple :',Immutable_var)
#Immutable_var[0] = 5
#print(Immutable_var)             #Кортежи (tuples) в Python — это упорядоченные коллекции элементов, которые, в отличие от списков, являются неизменяемыми. Это означает, что после создания кортежа его элементы нельзя изменить, добавить или удалить.
Mutable_var = [ 1, 2, 3, 'apple', False, "string"]
Mutable_var.append(True)
Mutable_var.extend(['coffee', 'donuts'])
Mutable_var.remove(False)
print('Mutable list :',Mutable_var)