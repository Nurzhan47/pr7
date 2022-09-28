import math

def area(shape):
    if shape == 1:
        base = int(input("Base of triange: "))
        height = int(input("Height of triange: "))
        print((height * base) / 2)
    elif shape == 2:
            length = int(input("Length of rectangle: "))
            width = int(input("Width of rectangle: "))
            print(length * width)
    else:
        radius = int(input("Radius of circle: "))
        print(math.pi * radius ** 2)
shape1 = int(input("Choose:\n1.Triange\n2.Rectangle\n3.Circle\n"))
area(shape1)
print('\n')

print('task1.2')
import random
def summa(n):
    sum = 0
    for i in n:
        sum += i
    return sum

def ar(n,sum):
    return sum/len(n)

for i in range(3):
    a = random.sample(range(90), 15)
    print(a)
    print(summa(a))
    print(ar(a,summa(a)))
print('\n')

print('task2.1')
def Triarea(a):
    return (math.sqrt(3) / 4) * a ** 2
a = int(input("Side of regular sheteugolnik: "))
print("Area of regular shesteugolnik is:", Triarea(a)*6)

print('task2.2')
def rectangle(length,width):
    return length * width
for i in range(3):
    a = int(input("first side: "))
    b = int(input("second side: "))
    print("area of recangle is:", rectangle(a,b))
print('\n')

print('Task3.1')
def hypotenuses(a,b):
    return math.sqrt(a**2 + b**2)

temp = []
for i in range(2):
        a = int(input("a: "))
        b = int(input("b: "))
        print("hypotenuses of triangle is:",hypotenuses(a,b))
        temp.append(hypotenuses(a,b))

if temp[0] > temp [1]:
    print("hypotrnuses of first triangle is bigger")
elif temp[1] > temp[0]:
    print("hypotrnuses of second triangle is bigger")
else:
    print("hypotrnuses of both triangles are same")
print('\n')
print('task3.2')
def sort(str):
    return ''.join(sorted(str))
print(sort("JOHNCENA TINDUN TINDUN"))

print('\n')
print('task 4')
def gcd(x,y):
    if (y == 0):
        return abs(x)
    else:
        return gcd(y, x % y)

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
d = int(input("D: "))
print(math.trunc(a*d / gcd(a*d,b*c)), "/", math.trunc(b*c / gcd(a*d,b*c)))
print('\n')
#2
print('task 5.1')
def eyob(x,y):
    if x > y:
        temp = x
    else:
        temp= y
    while True:
        if temp % x == 0 and temp % y == 0:
            eyob = temp
            break
        temp+= 1
    return eyob

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
d = int(input("D: "))
a =a/ gcd(a,b)
b =b/ gcd(a,b)
c =c/ gcd(c,d)
d =d/ gcd(c,d)
b2 = eyob(b,d)
d2 = b2
a *= b2 / b
c *= d2 / d
print(a - c, "/", b2)
print('\n')
print('task5.2')
def div(n):
    answer = []
    for i in range(1,n+1):
        if n % i == 0:
            answer.append(i)
    return answer
    
n = int(input("n: "))
print(div(n))

print('task 6.1')
a = int(input("a: "))
b = int(input("b: "))

print("gcd of a and b:",gcd(a,b))
print("eyob of a and b:",eyob(a,b))

print('task 6.2')
def Per21(a,b,c):
    s = (a + b + c) / 2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
d = int(input("D: "))
h = int(input("diagoal of (A,C): "))
print(Per21(a,b,h) + Per21(c,d,h))

print('task7.1')
def triangleArea(base,height):
    return (height * base) / 2
a = int(input("long base: "))
b = int(input("short base: "))
h = int(input("height: "))
t = int(input("leg: "))

print("Area:", triangleArea(a-b,h) + rectangle(b,h))

print('task7.2')
def decToOct(n):
    return '{:010o}'.format(n)

a = int(input())
print(decToOct(a))

print('task 8.1')
def d(n):
    ans = []
    for i in range(1,n+1):
        s = str(i)
        temp = True
        for j in s:
            if int(j) == 0:
                temp = False
            elif i % int(j) != 0:
                temp = False
        if temp:
            ans.append(i)
    return ans

n = int(input("n: "))
print(d(n))
print('task8.2')
def swaping(a):
    a[0],a[len(a)-1] = a[len(a)-1],a[0]
    return a

m = int(input("length of array: "))
A = []
for i in range(m):
    n = int(input("element of array: "))
    A.append(n)

print(A)
print(swaping(A))
print('task9.1')
def sumdig(n):
    s = str(n)
    sum = 0
    for i in s:
        sum += int(i)
    return sum

n = int(input("N: "))
sub = sumdig(n)
ans = 0
while n > 0:
    ans += 1
    n -= sub

print(ans)
print('task9.2')
def period(n):
    prd = 1
    for i in n:
        prd *= i
    return prd

for i in range(3):
    a = random.sample(range(98), 15)
    print(a)
    print(period(a))
    print(ar(a,summa(a)))
print('task10.2')
def reverce(s):
    s = s.split()[::-1]
    ans = []
    for i in s:
        ans.append(i)
    return ' '.join(ans)

s = input("Enter str to reverse: ")
print(reverce(s))

print('task11.1')
def isPrime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

n = int(input("n: "))

for i in range(n,2*n):
    if isPrime(i) and isPrime(i+2):
        print(i,i+2)
print('task 11.2')

def fndmax(arr, n):
    max = -1
    x = 0
    y = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > max:
                max = arr[i][j]
                x = i
                y = j
    return x,y

arr1 = [[1,2,3,4,],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
arr2 = [[12,24,36,14,],[45,62,7,38],[19,10,21,52],[53,84,35,26]]
print(arr1)
print(arr2)

max1 = fndmax(arr1,4)
max2 = fndmax(arr2,4)

arr1[max1[0]][max1[1]],arr2[max2[0]][max2[1]] =  arr2[max2[0]][max2[1]],arr1[max1[0]][max1[1]]
print(arr1)
print(arr2)

print('task 12.1')
def sumO(n):
    ans = 0
    for i in range(1,n+1):
        if n % i == 0:
            ans+= i
    return ans

n = int(input("N: "))
for i in range(n):
    a = sumO(i)
    for j in range (i+1,n):
        b = sumOFAllDivisors(j)
        if a == b:
            print(i,j)
            continue
print('task 13.1')
k = int(input("k: "))
for i in range(2,k):
    for j in range(k):
        if sumOfDigits(i)**j == i:
            print(i,j)
        elif sumOfDigits(i)*j > i:
            break
print('task15')
def Palindrome(n: int) -> bool:
    rev = 0
    i = n
    while i > 0:
        rev = rev * 10 + i % 10
        i //= 10
    return (n == rev)
def count(minn: int, maxx: int) -> None:
    for i in range(minn, maxx + 1):
        if Palindrome(i):
            print(i, end = " ")
if name == "main":
    count(1, 1000)def Palindrome(n: int) -> bool:
    rev = 0
    i = n
    while i > 0:
        rev = rev * 10 + i % 10
        i //= 10
    return (n == rev)
def count(minn: int, maxx: int) -> None:
    for i in range(minn, maxx + 1):
        if Palindrome(i):
            print(i, end = " ")
if name == "main":
    count(1, 1000)
