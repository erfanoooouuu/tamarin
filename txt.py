#Say "Hello, World!" With Python

if __name__ == '__main__':
    print("Hello, World!")


#What's Your Name?


#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)



#Python If-Else

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2 != 0:
        print("Weird")
    else:
        if n in range(2,6):
            print("Not Weird")
        elif n in range(6, 21):
            print("Weird")
        elif n >= 20:
            print("Not Weird")


#Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)


#Python: Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)


#Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(0, n):
        print(i**2)


#Print Function

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        print(i, end='')


#Find the Runner-Up Score! 

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(set(arr))
    arr.sort()
    print(arr[-2])


#Nested list

if __name__ == '__main__':
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append([name, score])
    soretd_list = sorted(scores, key= lambda item: float(item[1]),)
    
    
    for i in soretd_list:
        if i[1] != soretd_list[0][1]:
            sec = i
            break
    
    list_alphb = []
    
    for i in soretd_list:
        if sec[1] == i[1]:
            list_alphb.append(i)
    
    list_alphb.sort()
    for i in list_alphb:
        print(i[0])



#Lists


if __name__ == '__main__':
    N = int(input())
    arr = []
    list_funcs = ['insert', 'print', 'remove', 'append', 'sort', 'pop', 'reverse']
    for i in range(N):
        cmnd = input()
        splited_cmnd = cmnd.split()
        if splited_cmnd[0] not in list_funcs:
            print('wrong')
            break
        if splited_cmnd[0] == 'insert':
            arr.insert(int(splited_cmnd[1]), int(splited_cmnd[2]))
        elif splited_cmnd[0] == 'print':
            print(arr)
        elif splited_cmnd[0] == 'remove':
            arr.remove(int(splited_cmnd[1]))
        elif splited_cmnd[0] == 'append':
            arr.append(int(splited_cmnd[1]))
        elif splited_cmnd[0] == 'sort':
            arr.sort()
        elif splited_cmnd[0] == 'pop':
            arr.pop()
        elif splited_cmnd[0] == 'reverse':
            arr.reverse()



#tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))


#Power - Mod Power


a = int(input())
b = int(input())
m = int(input())
while m<0:
    m = int(input('plz give positive number!'))

print(a**b)
print(pow(a,b,m))


#Integers Come In All Sizes

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print((a**b) + (c**d))



#Input()


# Enter your code here. Read input from STDIN. Print output to STDOUT
input_range = input().split()

input_dovomi = input()

input_range = list(map(int, input_range))
x = input_range[0]
k = input_range[1]

int_out = 0
for i in range(0, k):
    int_out += x**k

eval_dovomi = eval(input_dovomi)

if int_out == k:
    print(True)
    
elif eval_dovomi == k:
    print(True)
else:
    print(False)


#Python Evaluation

# Enter your code here. Read input from STDIN. Print output to STDOUT

tet = input()
eval(tet)

#Map and Lambda Function


cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # base_kar = [0, 1]
    base_kar = []
    if n>2:
        base_kar = [0, 1]
        for i in range(0, n-2):
            fib_baadi = base_kar[-1] + base_kar[-2]
            base_kar.append(fib_baadi)
    else:
        if n==1:
            base_kar =[0]
        elif n==2:
            base_kar = [0,1]

            
    return base_kar
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))



#Decorators 2 - Name Directory

import operator

def person_lister(f):
    def inner(people):
        # complete the function
        listak = sorted(people, key= lambda item: int(item[2]),)
        mylist = []
        for i in listak:
            mylist.append(("Mr. " if i[3] == "M" else "Ms. ") + i[0] + " " + i[1])
        return mylist

    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')



#Write a function

def is_leap(year):
    leap = False
    
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
        
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))