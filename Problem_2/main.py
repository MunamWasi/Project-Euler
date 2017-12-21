sum = 2
fib = 1
fib_max = 2
temp = 0

while fib_max < 4000000:
    temp = fib_max
    fib_max = fib + fib_max
    fib = temp
    if fib_max % 2 == 0:
        sum += fib_max

print(sum)