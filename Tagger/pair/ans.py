count = 0
input1  = int(input())
input2 = int(input())
arr =  [['0' for i in range(input2)] for j in range(input2)]

for i in range(input2):
    for j in range(input2):
        if count < input1:
            arr[i][j] = count
            count +=1
        else:
            arr[i][j] = 0


print(arr)
