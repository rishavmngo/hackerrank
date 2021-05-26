def minion_game(string): 
    string = string.upper()
    vowel = "AEIOU"
    stuart_score = 0
    stuart_substring = [] 
    kevin_score = 0
    kevin_substring = []
    def occurance_list(c):
        list1 = []
        for i in range(c+1,len(string)+1):
            list1.append(string[c:i])
        return list1
    c = 0
    while c < len(string):
        if string[c] in vowel:
            temp = occurance_list(c)
            stuart_score += len(occurance_list(c))
            for x in temp:
                kevin_substring.append(x)
        else:
            temp = occurance_list(c)
            for x in temp:
                stuart_substring.append(x) 
        c += 1
    stuart_score = len(stuart_substring)
    kevin_score = len(kevin_substring)
    if kevin_score > stuart_score:
        print("Kevin",kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart",stuart_score)
    else:
        print("Draw")
