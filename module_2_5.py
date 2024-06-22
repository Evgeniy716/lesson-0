def get_matrix(n,m,value):
    matrix = []
    for i in range (n):
        matrix.append([])
        for j in range (m):
            matrix.append(value)

    return(matrix)
results1 = get_matrix(2,2,10)
results2 = get_matrix(3,5,42)
results3 = get_matrix(4,2,13)

print (results1)
print (results2)
print (results3)