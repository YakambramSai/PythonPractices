given_string = "a!!!b.c.d,e'f,ghi"
print("Input string: " + given_string)


def string_to_list(given_string):
    List = []
    for i in given_string:
        List.append(i)
    return List


def isAlphabet(x):
     return x.isalpha()


def swap(a, b):
    return b, a


def list_to_string(List):
    return ''.join(List)


def reverseString(given_string):
    char_list = string_to_list(given_string)
    # Initialize left and right pointers
    r = len(char_list) - 1
    l = 0
    while l < r:
        if  isAlphabet(char_list[l]):
            l+=1
        elif  isAlphabet(char_list[r]):
            r-=1
        else:
            char_list[l], char_list[r] = swap(char_list[l], char_list[r])
            l+=1
            r-=1
        # print(toString(LIST))
    return list_to_string(char_list)

reversed_string = reverseString(given_string)
print("Output string: " + reversed_string)