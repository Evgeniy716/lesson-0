first = int(input("Введите число: "))
second = int(input("Введите число: "))
third = int(input("Введите число: "))
if  first == second == third :
     print('3')
elif  first != second == third or first == second != third or first == third:
    print('2')
elif first != second != third :
    print('0')