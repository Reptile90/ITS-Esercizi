def fib_memo(n:int):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:

        return  int(fib_memo(n-1))+ (fib_memo(n-2))