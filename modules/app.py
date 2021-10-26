# from factorial import fact as fa
import factorial
import sys
import peculiar
import peculiar.fibo as fi

def main():
    res = factorial.fact(6)
    # res = fa(6)
    print(factorial.__name__)
    print(factorial.__version__)
    print(res)
    res = fi.fib(7)
    print(fi.__name__)
    print('Fibonacci = ', res)
    print(peculiar.__version__)
    print(peculiar.__name__)
    print(peculiar.__doc__)
    print(fi.__doc__)
    print(fi.fib.__doc__)
    # print(sys.path)

if __name__ == '__main__':
    main()
