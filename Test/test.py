number = 600851475143
value = 0
answer = 0
def isprime(x):
    if x > 1:
       # check for factors
       for i in range(2,x):
           if (x % i) == 0:
               return False
       return True
    else:
        return True


for i in range(775147):
    i+=1
    if 600851475143 % i == 0:
        if isprime(i):
            answer = i

print(answer)