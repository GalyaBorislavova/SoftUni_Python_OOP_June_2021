def even_parameters(func):
    message_error = "Please use only even numbers!"

    def wrapper(*args):
        try:
            evens = [el for el in args if el % 2 == 0]
            if len(evens) == len(args):
                result = func(*evens)
                return result
            else:
                return message_error
        except TypeError:
            return message_error

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
