import time

# Декоратор - функция, которая принимает в кажестве аргумента другую функцию и расширяет ее функционал

def getNOD (a, b): # алгоритм Евклида (для поиска найбольшего общего делителя 2 натцральных чисел)
    while a != b:
        if a > b: a -= b
        else: b -= a
    return a

def getFastGOOD(a, b):
    if a < b : a,b = b,a
    while b : a,b = b, a%b
    return a

# Нужно создать тест, для проверки скорости работы функции (в виде декоратора)

def testTime(fn):
    def wrapper(*args): # обертка, которая разширяет функционал функции fn
        st = time.time()
        fn(*args)
        dt = time.time() - st
        print(f"Время работы : {dt}")
    return wrapper # возвращает в переменную, нашую обертку (которую и вызывает)

test1 = testTime(getNOD) # есть возможность создать новое имя и потом с ним работать
test2 = testTime(getFastGOOD)
test1(10000,2) # передает данные, в аргументы функции wrapper, которая передает аргументы в fn (getNOD)
test2(10000,2)

#------------------------------------- Синтаксис декораторов с помощью @ -----------------------------------------------

def testTime(fn):
    def wrapper(*args):
        st = time.time()
        res = fn(*args) # так как функции возвращают значение
        dt = time.time() - st
        print(f"Время работы : {dt}")
        return res # возвращаем его, чтобы не потерять
    return wrapper

@testTime # автоматом в testTime, передаем функцию (getNod) в качестве аргумента (fn)
def getNOD (a, b):
    while a != b:
        if a > b: a -= b
        else: b -= a
    return a

@testTime
def getFastGOOD(a, b):
    if a < b : a,b = b,a
    while b : a,b = b, a%b
    return a

res = getNOD(10000,2) # вызывается декоратор testTime, с функцией getNOD
res1 = getFastGOOD(10000,2)

print(f"{res}\n{res1}")

#-----------------------------------------------------------------------------------------------------------------------

