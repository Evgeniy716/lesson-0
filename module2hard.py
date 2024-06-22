n = []
s = int(input('Введите число от 3 до 20: '))
for i in range (1,21):
    for j in range(1,21):
        q = i+j
        if s%q==0 and i<j:
            n.append(i)
            n.append(j)
print(*n)
