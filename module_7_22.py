def custom_write (file_name, strings):
    file = open(file_name,"w",encoding="utf-8")
    strings_positions ={}
    pos_str = 1
    pos_byte = 0
    for string in strings:
        file.write(string + '\n')
        strings_positions[(pos_str,pos_byte)] = string
        pos_str +=1
        pos_byte = file.tell()
    file.close()
    return strings_positions




info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

    # Вывод
    # на
    # консоль:
    # ((1, 0), 'Text for tell.')
    # ((2, 16), 'Используйте кодировку utf-8.')
    # ((3, 66), 'Because there are 2 languages!')
    # ((4, 98), 'Спасибо!')