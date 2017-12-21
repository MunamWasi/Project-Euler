number = 600851475143

factors = [0]

def isprime(x):
    for i in range(x):
        i+=1
        if x % i == 0:
            return False
    return True 

for i in range(600851475143):
    i+=1
    if 600851475143 % i == 0:
        if isprime(i):
            factors.append(i)
value = sum(factors)

print value

