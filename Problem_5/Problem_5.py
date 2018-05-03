increase = 20

i = 2

while True:
    if increase % i == 0:
        if i == 20:
            print(increase)
            break
        i += 1
    else:
        i = 1
        increase += 20