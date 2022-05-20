def end_zeros(num):
    num2 = list(str(num))
    new_list = []
    new = 0

    for x in num2:
        new_list.append(int(x))

    for x in new_list[::-1]:
        if x == 0:
            new +=1
        else:
            break
        
    return new


if __name__ == "__main__":
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
