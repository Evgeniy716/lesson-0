my_dict = {'Ivan':1991,'Igor':1999,'Max':2000,'Lev':1990}
print('Dict:',my_dict)
print('Existing valye:',my_dict['Igor'])
print('Not existing value:',my_dict.get('Nikolay','Отсутствует в списке'))
my_dict.update({'Aleksandr': 1995,'Petr': 1991})
a = my_dict.pop('Ivan')
print('Deletted value:',a)
print('Modified dictionary:', my_dict)
my_set = {1,2,3,3,'Ivan','Ivan',True}
print('Set :',my_set)
my_set.add('Petr')
my_set.add(45)
my_set.discard(1)
print('Modified set:',my_set)
