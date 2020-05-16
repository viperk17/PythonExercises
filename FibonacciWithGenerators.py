# Fibonacci Series With Generators

def fib(number):
    a=0
    b=1
    for i in range(number):
        print("This is ", a)
        yield a
        
        tmp = a
        a = b
        b = tmp + b

for x in fib(7):
    print(x)