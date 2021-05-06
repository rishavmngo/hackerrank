b = int(input())
a = {}
while b > 0:
    some = input()
    some = some.split()
    var = some.pop(0)
    some = [float(x) for x in some]
    a[var] = some
    b -= 1
name_avg = input()
avg = 0
for x in a[name_avg]:
    avg += x
avg = avg/3
print("{:.2f}".format(avg))

