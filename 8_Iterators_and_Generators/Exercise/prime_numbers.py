from typing import List


def is_prime(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, (number//2) + 1):
        if number % i == 0:
            return False
    return True


def get_primes(nums: List[int]):
    for num in nums:
        if is_prime(num):
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))