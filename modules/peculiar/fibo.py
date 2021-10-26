"""The Fibo module's documentation string
The module's documentation string
The module's documentation string
The module's documentation string"""
def fib(n):
    """The Fib function's documentation string"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    n = int(input())
    print(fib(n))
