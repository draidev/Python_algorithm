def fib1(n):
    if n<=2: return 1
    return fib1(n-1)+fib(n-2)

def fib2(n):
    if n<=2: return 1
    a, b = 1, 1
    for i in range(n-2):
        a, b = a+b, a
        return a

cache = {}
def fib3(n):
    if n in cache:
        return cache[n]
    if n <= 2:
        result = 1
    else: 
        result = fib3(n-1) + fib3(n-2)
    cache[n] = result
    return result

def fib4(n):
    if n<=2: return 1
    fib_list = [1,1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1], filb_list[-2])
    return fib_list[-1]

