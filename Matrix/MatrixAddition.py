# Program to add two matrices using nested loop

X = [[2,7,3],
    [4 ,5,6],
    [7 ,4,9]]

Y = [[1,8,1],
    [6,7,7],
    [4,5,6]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

# OR
# result = [[X[i][j] + Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]

for r in result:
   print(r)
