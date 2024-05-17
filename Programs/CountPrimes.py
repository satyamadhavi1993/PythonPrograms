def is_prime(number):
    if number % 2 == 0:
        return False
    for i in range(3, number//2 + 1):
        if number % i == 0:
            return False
    return True    
    

def count_primes(limit):
    print(2)
    count = 1
    for i in range(3, limit + 1, 2):
        if is_prime(i):
            count += 1
            print(i)
    print('Count is ', count)

count_primes(100)
