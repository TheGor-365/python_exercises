def fizz_buzz(begin, end):
    if begin > end:
        return ''
    elif begin == end:
        return str(begin)
    result = []
    for i in range(begin, end):
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
