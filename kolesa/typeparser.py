def parseToFloat(string):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
    converted = []
    for letter in string:
        if letter in numbers:
            converted.append(letter)


    return(float(''.join(converted)))

def parseToInt(string):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    converted = []
    for letter in string:
        if letter in numbers:
            converted.append(letter)


    return(int(''.join(converted)))