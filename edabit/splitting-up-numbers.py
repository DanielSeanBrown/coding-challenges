# available at: https://edabit.com/challenge/Wd9cCvFKC3fHzgqSx

def num_split(num):

    '''Takes an integer and returns a list of its decimal components'''

    negative = False
    split = []
    counter = 0

    # recognise negative values
    if num < 0:
        negative = True
        num *= -1

    # extract values
    for digit in str(num)[::-1]:
        split.insert(0, int(digit) * 10 ** counter)
        counter += 1

    # ammend signs if needed
    if negative:
        for digit in range(len(split)):
            split[digit] *= -1
    
    return(split)
        
# Tests as seen on website
assert num_split(39) == [30, 9]
assert num_split(-434) == [-400, -30, -4]
assert num_split(100) == [100, 0, 0]
assert num_split(3929) == [3000, 900, 20, 9]
assert num_split(10293) == [10000, 0, 200, 90, 3]
assert num_split(900) == [900, 0, 0]
assert num_split(-100)== [-100, 0, 0]
