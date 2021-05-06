def swap_case(inp):
    p = ""
    for i in inp:
        if i.islower():
            p += i.upper()
        elif i.isupper():
            p += i.lower()
        else:
            p += i
    return p

