def mutate_string(string, position, character):
    string = [x for x in string]
    string[position] = character
    string = "".join(string)
    return string

