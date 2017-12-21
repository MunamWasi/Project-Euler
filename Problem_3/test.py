number = 600851475143

factors = []

for i in range(600851475143):
    if 600851475143 % i == 0:
        if isprime(i):
            factors.append(i)

def isprime(x: int) -> bool:
    for i in range(x):
        i+=1
        if x % i == 0:
            return False
    return True 

return factors