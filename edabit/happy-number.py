# challange available at: https://edabit.com/challenge/J9fCHDa3yYJWnK3A7

def is_happy(num):
    if num == 1:
        return True
    elif num == 4:
        return False
    else:
        new_num = 0
        for digit in str(num):
            new_num += int(digit)**2
        return is_happy(new_num)


assert is_happy(67) == False
assert is_happy(89) == False
assert is_happy(139) == True
assert is_happy(1327) == False
assert is_happy(2871) == False
assert is_happy(3970) == True
