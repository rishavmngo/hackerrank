b = input()
list1 = []
a = input()
list1 = [int(x) for x in a.split()]
list1 = list(set(list1))
list1.sort()
print(list1[-2])
