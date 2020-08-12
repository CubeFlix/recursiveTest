def isprime(num):
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return False
    return True

def prime_factors(n):
    if isprime(n):
        return [n]
    for i in range(1, int(n/2+1)):
        if int(n/i) == n/i:
            if isprime(int(n/i)):
                return [int(n/i)] + prime_factors(i)
            
