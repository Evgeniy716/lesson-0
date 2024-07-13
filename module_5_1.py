class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors


    def go_to(self, new_floor,):
        for i in range(new_floor):
            i+=1
            if i <= 18:
                print(i)
            else:
                print("Такого этажа не существует")






h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
# h2.go_to(10)
