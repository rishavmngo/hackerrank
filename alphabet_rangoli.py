import string
alpha = string.ascii_lowercase
size = 3
char = ""
while size > 0:
    char += f"-{alpha[size - 1]}-"
    size -= 1

print(char)

