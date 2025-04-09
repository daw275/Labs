import time

def memoize(func):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result
    return wrapper

def recur_fibo(n):
    if n <= 1:
        return n
    return recur_fibo(n-1) + recur_fibo(n-2)

@memoize
def recur_fibo_memo(n):
    if n <= 1:
        return n
    return recur_fibo_memo(n-1) + recur_fibo_memo(n-2)

def main():
    n = 35

    start_naive = time.time()
    naive_result = recur_fibo(n)
    end_naive = time.time()
    print(f"Naive Fibonacci of {n}: {naive_result}")
    print(f"Naive recursion time: {end_naive - start_naive:.4f} seconds\n")

    start_memo = time.time()
    memo_result = recur_fibo_memo(n)
    end_memo = time.time()
    print(f"Memoized Fibonacci of {n}: {memo_result}")
    print(f"Memoized recursion time: {end_memo - start_memo:.4f} seconds")

if __name__ == "__main__":
    main()
