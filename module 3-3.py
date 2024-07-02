def print_params(a=1,b='строка', c=True):
    print(a,b,c)

print_params(1,'строка', True)
print_params(5,7,9)
print_params(b=25)
print_params(c=[1,2,3,])
value_list = [5,'строка',False]
value_dict = {'a':9,'b':"Hello",'c':99}
print_params(*value_list)
print_params(**value_dict)
value_list_2=["Yes",666]
print_params(*value_list_2,42)