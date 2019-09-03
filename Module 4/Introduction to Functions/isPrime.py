def isPrime(num):
    prime = True
    for i in range(2, num//2 + 1):
        if num%i == 0:
            prime = False
    return prime

print('Primes under 20 are: ')
small_primes = []
for i in range(2,19):
    if isPrime(i):
        small_primes.append(i)
print(small_primes)
    
