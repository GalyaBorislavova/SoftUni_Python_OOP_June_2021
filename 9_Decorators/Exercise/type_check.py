def type_check(t):
    error_message = "Bad Type"

    def decorator(func):
        def wrapper(*args):
            if isinstance(*args, t):
                return func(*args)
            else:
                return error_message
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
