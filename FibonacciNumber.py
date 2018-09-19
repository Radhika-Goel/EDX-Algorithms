#/usr/bin/python2
#memonization
def fib(n):
    if n in memo:
        return memo[n]
    if n == 0:
        f = 0
    elif n <= 2:
        f = 1
    else:
        f = fib(n-1) + fib(n-2)
    memo[n] = f
    return f

n = int(raw_input())
memo = {}
print fib(n)

def fib1(n):
    for i in range(n+1):
       if i == 0:
            f = 0
       elif i <= 2:
            f = 1
       else:
            f = memo1[i-1] + memo1[i-2]
       memo1[i] = f
    #print memo1
    return memo1[n]
#Fibonacci Table
n = int(raw_input())
memo1 = [0]*(n+1)
print fib1(n)

#Last Digit of Fibonacci Number
def fib(n):
    if n in memo:
        return memo[n]
    if n == 0:
        f = 0
    elif n <= 2:
        f = 1
    else:
        f = fib(n-1) + fib(n-2)
    memo[n] = f
    return f%10

n = int(raw_input())
memo = {}
print fib(n)