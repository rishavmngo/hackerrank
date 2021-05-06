number = int(input())
list1 = []
for i in range(0,number):
    list1.append([input(),float(input())])
list1.sort(key=lambda x: x[1])
lowest = list1[0][1]
for x in list1:
    if x[1] > lowest:
        lowest = x[1]
        break
list2 = []
for x in list1:
    if x[1] == lowest:
        list2.append(x)
list2.sort(key=lambda x: x[0])
for x in list2:
    print(x[0])

