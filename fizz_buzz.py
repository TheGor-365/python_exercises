def fizz_buzz(begin, end):
    result = []
    if begin > end:
        return ''
    for i in range(begin, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append('FizzBuzz')
        elif i % 3 == 0:
            result.append('Fizz')
        elif i % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(i))
    final = ' '.join(result)
    return final


print(fizz_buzz(7, 7))

# def test_fizz_buzz():
#     assert fizz_buzz(1, 0) == ''
#     assert fizz_buzz(7, 7) == '7'
#     assert fizz_buzz(1, 5) == '1 2 Fizz 4 Buzz'
#     assert fizz_buzz(11, 20) == '11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz'
