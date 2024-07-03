# def find_max (list_):                  #Поиск максимального числа из списка
#     max_ = list_[0]
#     for i in list_:
#         if i > max_:
#             max_ = i
#     return max_
#
# print(find_max([1,54,12,-1,500,4]))

# def count_even(list_):                 # Проверка на четность.
#     counter = 0
#     for i in list_:
#         if i % 2 == 0:
#             counter = counter + 1
#     return counter
#
#
# print(count_even([2,3,4,5,6,7,8]))

                                        #Уникальный список.
def unique(list_):
    new_list = []
    for i in list_:
        if i not in new_list:
            new_list.append(i)
    return new_list
print(unique([1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]))



