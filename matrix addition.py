x= [[2,5,4],
     [6,7,9],
     [5,3,2]]

print(x)

y= [[1,9,5],
    [2,7,4],
    [1,3,2]]

print(y)

result =          [[0,0,0],
                   [0,0,0],
                   [0,0,0]]

print(result)

                      

for i in range (len(x)):
     for j in range (len(x[0])):
          result[i][j] = x[i][j] + y[i][j]
          

print(result)           