def palindrome_check(number):
    reverse = number[::-1]
    if reverse == number:
        return True
    return False
        
answer = 0

for number_1 in range(100, 999):
    for number_2 in range(100,999):
        palindrome = (number_1 * number_2)
        if palindrome_check(str(palindrome)):
            if (palindrome > answer):
                answer = palindrome
                print(palindrome)