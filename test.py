inp = input()
char = ".|."
inp = inp.split()
m = int(inp[0])
n = int(inp[1])
counter = (m - 1)/2
i = 1
while counter > 0:
    print((char*i).center(n,'-'))
    counter -= 1
    i += 2
print("WELCOME".center(n,"-"))
counter = (m - 1)/2
i = i - 2
while counter > 0:
    print((char*i).center(n,'-'))
    counter -= 1
    i -= 2
