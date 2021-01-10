x = [[1,2,3],
     [1,2,3],
     [1,2,3]]

print(x)

y =  [[1,2,3],
      [1,2,3],
      [1,2,3]]

print(y)  

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

print(result)

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range (len(y)):
            result[i][j] = result[i][j] + x[i][k] * y[k][j]

for x in result:
    print(x)           
