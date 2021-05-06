s = input()

response_alpha = "False"
response_num = "False"
for x in s:
    if x.isalpha():
        response_alpha = "True"
    elif x.isdigit():
        response_num = "True"
if response_alpha == "True" or response_num == "True":
    print("True")
else:
    print("False")
print(response_alpha)
print(response_num)
response_lower = "False"
response_upper = "False"
for x in s:
    if x.islower():
        response_lower = "True"
    elif x.isupper():
        response_upper = "True"
print(response_lower)
print(response_upper)
