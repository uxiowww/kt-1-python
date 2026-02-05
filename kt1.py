print("тест: солнце желтое? 1 1) да 2) нет 3) мб")
user_input = input("Введите номер: ")

match user_input:
     case "1":
         print("no")
    case "2":
         print("yes")
    case "3":
        print("no")
    case _:
        print("Пожалуйста, введите 1, 2 или 3")

print("2+2 1) 4 2) 7 3) 5")
user_input = input("Введите номер: ")

match user_input:
    case "1":
        print("yes")
    case "2":
        print("no")
    case "3":
        print("no")
    case _:
        print("Пожалуйста, введите 1, 2 или 3")

print(" my name? 1 1) crazyfrog2001 2) ты кто 3) dasha")
user_input = input("Введите номер: ")

match user_input:
    case "1":
        print("no")
    case "2":
        print("no")
    case "3":
        print("yes")
    case _:
        print("Пожалуйста, введите 1, 2 или 3")

print(" мои навыки в разработке? 1 1) amazing 2) terrible 3) beautiful")
user_input = input("Введите номер: ")

match user_input:
    case "1":
        print("no")
    case "2":
        print("yes")
    case "3":
        print("no")
    case _:
        print("Пожалуйста, введите 1, 2 или 3")

print("тест: spiderman cool? 1) да 2) нет 3) мб")
user_input = input("Введите номер: ")

match user_input:
    case "1":
        print("yes")
    case "2":
        print("no")
    case "3":
        print("no")
    case _:
        print("Пожалуйста, введите 1, 2 или 3")

print("6+7  1) 13  2) 67 3) 100")
user_input = input("Введите номер: ")

match user_input:
    case "1":
        print("yes((")
    case "2":
        print("noo(")
    case "3":
        print("no")
    case _:
        print("Пожалуйста, введите 1, 2 или 3")

print("a,b,c.... 1) h 2) d 3) e")
user_input = input("Введите номер: ")

match user_input:
    case "1":
        print("no")
    case "2":
        print("yes")
    case "3":
        print("no")
    case _:
        print("Пожалуйста, введите 1, 2 или 3")

print(" zelenii nyasha 1) kriper 2) man 3) steve")
user_input = input("Введите номер: ")

match user_input:
    case "1":
        print("yes")
    case "2":
        print("no")
    case "3":
        print("no")
    case _:
        print("Пожалуйста, введите 1, 2 или 3")




#zadanie 2

import math

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

D = b*b - 4*a*c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print("x1 =", x1)
    print("x2 =", x2)
elif D == 0:
    x = -b / (2*a)
    print("x =", x)
else:
    print("Нет корней")


#zadanie3

ch = 0  
n = 0  

x = int(input())
while x != 100:
    if x % 2 == 0:
        ch += x
        n += 1
    x = int(input())

if n > 0:
    print(ch / n)
else:
    print(0)


n = int(input("scok bydet clov"))  


for i in range(n):
    word = input()  
    if word[0] not in "ABCabc":
        print("NO")
        break
else:
    print("YES")
