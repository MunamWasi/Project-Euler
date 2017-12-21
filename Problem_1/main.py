'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

'''
def main():
    multiples = [3, 5]
    total = 0
    for n in range(1000):
        if any(n % multiple == 0 for multiple in multiples):
            total += n
    print(total)

main()
'''
'''
def corners(n):
    upper_right = (2*n - 1)**2 + (2*n - 1) + 1
    upper_left = upper_right + 1*(2*n - 1)
    bottom_right = upper_right + 2*(2*n - 1)
    bottom_left = upper_right + 3*(2*n - 1)
    print(upper_right, upper_left, bottom_right, bottom_left)
'''

def corners(n):
    base_val = (2*n - 1)**2 + (2*n - 1) + 1
    return [base_val + c*(2*n - 1) for c in range(4)]
    
corners(1000)
