def is_perfect(number):
    sum = 0
    if number == 0:
        return False
    for i in range(1, number):
        if number % i == 0:
            sum += i
    return sum == number


print(is_perfect(0))

# def test_is_perfect():
#     assert is_perfect(6)
#     assert is_perfect(28)
#     assert is_perfect(8128)


# def test_not_is_perfect():
#     assert not is_perfect(-6)
#     assert not is_perfect(-28)
#     assert not is_perfect(0)
#     assert not is_perfect(1)
#     assert not is_perfect(8127)
