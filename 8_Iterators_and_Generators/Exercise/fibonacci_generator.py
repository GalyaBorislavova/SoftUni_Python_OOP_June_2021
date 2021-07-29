# way 1
def fibonacci_iter():
    fib_num_1, fib_num_2 = 0, 1
    yield fib_num_1
    yield fib_num_2

    next_num = fib_num_1 + fib_num_2
    fib_num_1, fib_num_2 = fib_num_2, next_num
    while True:
        yield next_num
        next_num = fib_num_1 + fib_num_2
        fib_num_1, fib_num_2 = fib_num_2, next_num


# way 2
def fibonacci():
    i = 0
    while True:
        yield fibonacci_n(i)
        i += 1


def fibonacci_n(n):
    if n == 0 or n == 1:
        return n
    return fibonacci_n(n - 1) + fibonacci_n(n - 2)


generator_with_recursion = fibonacci()
for i in range(30):
    print(next(generator_with_recursion))

generator = fibonacci_iter()
for i in range(100):
    print(next(generator))




