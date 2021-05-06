num = int(input())
t = ()
x = input()
x = x.split()
for i in x:
    t += (int(i),)
print(hash(t))

