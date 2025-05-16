
def shift_left(a, b):
    #https://www.codewars.com/kata/5bdc191306a8a678f6000187

    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 and j >= 0 and a[i] == b[j]:
        i -= 1
        j -= 1

    return (i + 1) + (j + 1)



def explode(arr):
    #https://www.codewars.com/kata/57eb936de1051801d500008a

    a, b = arr
    a_is_num = isinstance(a, (int, float))
    b_is_num = isinstance(b, (int, float))

    if a_is_num and b_is_num:
        score = a + b
    elif a_is_num:
        score = a
    elif b_is_num:
        score = b
    else:
        return 'Void!'

    return [arr] * score