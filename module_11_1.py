import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import requests

###################PANDAS###########################################
# df = pd.DataFrame({"equirment": ["Обрабатывающий центр", "Портально фрезерный с ЧПУ", "Токарно фрезерный с ЧПУ"],
# "model": ["VMB 1250", "Ск6П250", "1740f2d"],
# "quantity": [5, 10, 15],
# "repair": [2, 4, 5]})
#
# fig = plt.figure(figsize =(10,5))
# plt.bar(df["equirment"],df["repair"])
# plt.xlabel('Общее количество оборудования')
# plt.ylabel('Количество оборудования на ремонте')
# plt.title('Количество неисправного оборудования')
# plt.show()
# df.to_excel('prostoy_obor.xlsx',index=False)



# ############################NUMPY##########################################
# a = np.array([1, 2, 3])
# b = np.array([7, 9, 9])
# # c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# # print(a)
# # print(b)
# # print(c)
# print(a + b)
# e = np.random.randint(-5, 10, size=(4, 4))
# print(e)
# #
# #                                                        #создание массивов
# z = np.array([[6,5,4,], [3,2,1]])
# #                                                        #объединение массивов
# d = np.vstack([b,z])
# print(d)
#
# filedata = np.genfromtxt('data.txt', delimiter=' ')         #чтение данных из файла
# filedata = filedata.astype('int32')
# print(filedata)


################################PILLOW############################################

from PIL import Image,ImageFilter

img = Image.open("robot.jpg")

img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
img.save("new_robot.jpg")

img = Image.open("new_robot.jpg")

img = img.filter(ImageFilter.BLUR)
img.save("new_robot2.jpg")

img = Image.open("new_robot2.jpg")

img = img.resize((img.width//2, img.height//2))
img.save("new_robot3.jpg")

img = Image.open("new_robot3.jpg")

img.show()