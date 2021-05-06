def wrap(s, num):
    count = 0
    result = ""
    for x in s:
        count += 1
        result += x
        if count == num:
            result += '\n'
            count = 0
    return result


