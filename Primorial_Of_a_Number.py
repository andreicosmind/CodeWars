'''Is similar to factorial of a number, In primorial, not all the natural numbers get multiplied, only prime numbers are multiplied to calculate the primorial of a number. It's denoted with P#
Task
Given a number N , calculate its primorial
Notes
Only positive numbers will be passed (N > 0)'''

def prime(a):
    for x in range(2, a//2+1):
        if a % x == 0: return False
    return True
        
def num_primorial(n):
    first = 2
    primes = []
    while len(primes)!= n:
        if first == 2:
            primes.append(first)
        else:
            if prime(first) == True:
                primes.append(first)
        first+=1
    prod = 1
    for x in primes:
        prod *= x
    return prod
