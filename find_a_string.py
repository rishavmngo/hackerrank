def count_substring(string, sub_string):
    count = 0
    i = 0
    for x in string:
        string = string[i:]
        index = string.find(sub_string)
        if index != -1:
            count += 1
            i = index + 1
        else:
            break
    return count
