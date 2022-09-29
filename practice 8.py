
print('task1.1')
import random
N=int(input("Enter n: "))
A=[[random.randrange(15) for i in range(N)] for j in range(N)]
print(A)
summ = 0
count= 0
for i in range(len(A) - 1):
    for j in range(i + 1, len(A[i])):
        if A[i][j] > 0:
            summ += A[i][j]
            count += 1
print("Sum of positive numbs: ", summ)
print("Count of pos. numbs: ", count)

print('task1.2')
import random
N = int(input())
M = int(input())
B = [[random.randrange(15) for i in range(M)] for j in range(N)]
for i in B:
    for j in i:
        print(j, end=" ")
    print()
for i, y in enumerate(B):
    max = min = 0
    for j, x in enumerate(y):
        if x > y[max]:
            max = j
        if x < y[min]:
            min = j
    y[max], y[0] = y[0], y[max]
    y[min], y[-1] = y[-1], y[min]
print(B)


print('task2.1')
#2)
N = 3
A = [[2, 7, 6],[9, 5, 1],[4, 3, 8]]
A = [[4, 3, 3], [3, 4, 3], [3, 3, 4]]
A = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]

s = 0
for i in range(N):
    s += A[0][i]

b = "YES"
for i in range(N):
    s1 = 0
    s2 = 0
    for j in range(N):
        s1 += A[i][j]
        s2 += A[j][i]
    if s1 != s or s2 != s:
        b = "NO"
        break

print(b)



print('task2.2')
N = 3
M = 4

A = [[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]
print("Current matrix: ")
for i in A:
    for j in i:
        print(j, end=" ")
    print()
print()

for i in range(N):
    tmp = A[i][0]
    A[i][0] = A[i][M-1]
    A[i][M-1] = tmp

for i in range(N):
    for j in range(M):
        print("%2d " % A[i][j], end='')
    print()

print('task3.1')
N = int(input("Enter N: "))
array=[[int(input()) for i in range(N)] for k in range(N)]
def transpose(mat, tr, N):
    for i in range(N):
        for j in range(N):
            tr[i][j] = mat[j][i]
def isSymmetric(mat, N):
   tr = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]
   transpose(mat, tr, N)
   for i in range(N):
        for j in range(N):
            if (mat[i][j] != tr[i][j]):
                return False
            return True
if (isSymmetric(array, 3)):
    print("Yes")
else:
    print("No")
print('task3.2')
N = int(input("Enter N: "))
M = int(input("Enter M: "))
array=[[int(input()) for i in range(N)] for k in range(M)]
max = float('-inf')
tempimax=0
tempkmax=0
for i in range(0,M):
    for k in range(0,N):
        if max<array[i][k]:
            max = array[i][k]
            tempimax =i
            tempimin =i
temp = array[0][0]
array[0][0]=max
array[tempimax][tempkmax] = temp
for i in range(0,M):
    for k in range(0,N):
        print(array[i][k] , end=" ")
    print("")

print('task4.1')
N = int(input("Enter N: "))
M = int(input("Enter M: "))
array=[[int(input()) for i in range(N)] for k in range(M)]
summin = float('inf')
tempsum=0
max=0
min=0
summax = float('-inf')
for i in range(0,M):
    for k in range(0,N):
        tempsum += array[i][k]
    if summin>tempsum:
        summin = tempsum
        min = i
    if summax<tempsum:
        summax = tempsum
        max = i
    tempsum = 0
print("sum of min row: " , summin)
for i in range(0,N):
   print(array[min][i])
print("sum of max row: " , summax)
for i in range(0,N):
    print('array[max][i])')


print('task4.2')
N = int(input("Enter N: "))
array=[[int(input()) for i in range(N)] for k in range(N)]
for i in range(0,N-1):
    for k in range(0,N):
        if array[i][k]>0:
            array[i][k]=1
        elif array[i][k]<0:
            array[i][k]=0
for i in range(0,N):
    for k in range(0,N):
        print(array[i][k] , end=" ")
    print("")
print('task5.1')
import random
n=int(input("Enter size: "))
m=int(input("Enter size 2: "))
a=[[random.randrange(10) for i in range(n)] for j in range(m)]
print(list(map(sorted, a)))

def qsort(a): 
    if len(a) <= 1:
        return a
    else:
        return qsort( [x for x in a[1:] if x < a[0]]) + [a[0]] + qsort([x for x in a[1:] if x >= a[0]] )
qsort(a)


print('task6.1')
N = int(input("Enter N: "))
M = int(input("Enter M: "))
array=[[int(input()) for i in range(N)] for k in range(M)]
max = float('-inf')
min = float('inf')
temp = 0
for i in range(0,M):
    for k in range(0,N):
        if max< array[i][k]:
            max = array[i][k]
            temp = k
    print("The biggest number in row:" ,temp," is: " , max)
    max = 0
for i in range(0,M):
    for k in range(0,N):
        if min>array[i][i]:
            min = array[i][i]
    print("The biggest number in column:" ,i," is: " , min)
    min = float('inf')



print('task6.2')
import random
n=int(input("Enter n: "))
arr=[[random.randrange(10) for i in range(n)] for j in range(n)]
for i in arr:
    print(i)
print()
 
a = sum(arr, [])
max1 = int(max(a[::n+1]))
max2 = int(max(a[n-1::n-1][:n]))
if max1 > max2:
    i1 = j1 = a[::n+1].index(max1)
else:
    i1 = a[n-1::n-1][:n].index(max2)
    j1 = n - 1 - i1
arr[n//2][n//2], arr[i1][j1] = arr[i1][j1], arr[n//2][n//2]
 
for i in arr:
    print(i)

print('task7,1')
matrix = [
       [1, 2, 3],
       [0, 6, 4],
       [0, 0, 6] ]
correct = []
for i in range(0,3):
    for k in range(i,3):
        correct.append(matrix[i][k])
for i in range(0,len(correct)):
    print(correct[i],end=" ")

print('task7,2')
N = int(input("Enter N: "))
M = int(input("Enter M: "))
array=[[int(input()) for i in range(N)] for k in range(M)]
arr = []
count = 0
for i in range(0,M):
    for k in range(0,N):
        if i==k:
            arr.append(array[i][k])
for i in range(0,len(arr)):
    count+=arr[i]
for i in range(0,len(arr)):
    if arr[i]%2 == 1:
        arr[i] = arr[i]/count
    print(arr[i],end="-")

    print('task8.1')
N = int(input("Enter N: "))
M = int(input("Enter M: "))
array=[[int(input()) for i in range(N)] for k in range(M)]
K = int(input("Enter k: "))
for i in range(0,M):
    for k in range(0,N):
        if i==k:
            array[K][i] = array[i][i]
for i in range(0,M):
    for k in range(0,N):
        print(array[i][k],end=" ")
    print(" ")
