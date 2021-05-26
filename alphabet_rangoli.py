import string
def print_rangoli(size):
    alpha = " " + string.ascii_lowercase
    char = ""
    list1 = []
    
    
    for i in reversed(range(1,size + 1)):
        first = i
        char = ""
        first_c = size
        second = []
        while first < size:
            char += alpha[first_c]
            second = list(reversed(char))
            first_c -= 1
            first += 1
        char += alpha[i]
        char += "".join([x for x in second])
        char = "-".join([x for x in char])
        list1.append(char.center((size * 4) - 3, '-'))
        
    final = list1[0:len(list1) - 1] 
    final.append(list1[-1])
    for i in reversed(list1[0:len(list1) - 1]):
        final.append(i)
    
    
    for i in final:
        print(i)
    
print_rangoli(int(input()))
