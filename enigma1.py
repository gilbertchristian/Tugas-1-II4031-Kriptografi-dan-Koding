from itertools import cycle

slow_list = [21, 3, 15, 1, 19, 10, 14, 26, 20, 8, 16,
            7, 22, 4, 11, 5, 17, 9, 12, 23, 18, 2, 25, 6, 24, 13]
medium_list = [20, 1, 6, 4, 15, 3, 14, 12, 23, 5, 16, 2,
            22, 19, 11, 18, 25, 24, 13, 7, 10, 8, 21, 9, 26, 17] 
fast_list = [8, 18, 26, 17, 20, 22, 10, 3, 13, 11, 4,
            23, 5, 24, 9, 12, 25, 16, 19, 6, 15, 21, 2, 7, 1, 14]    

def rotate(list):
    init = list[0]
    i=0
    while i !=len(list)-1:
        list[i] = list [i+1]
        i+=1
    list[i] = init
    return(list)

def slow_rotor(pos):
    for i in range(len(slow_list)):
        if pos == slow_list[i]:
            return(i)


def medium_rotor(pos):
    for i in range(len(medium_list)):
        if pos == medium_list[i]:
            return(i)


def fast_rotor(pos):
    for i in range(len(fast_list)):
        if pos == fast_list[i]:
            letter_convert = chr(i + 97)
            return(letter_convert)

def letter(plaintext):
    listtext = list(plaintext)
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    num_letter = []

    for i in range(len(listtext)): 
        for j in range (26):
            if alphabet[j] == listtext[i]:
                num_letter.append(j)
    print(num_letter)
    return (num_letter)

def search(rotor, key):
    cycle = []
    alphabet = list('abcdefghijklmnopqrstuvwxyz')

    for i in range (26):
        if alphabet[i] == key:
            num_key = i + 1
            break
    for i in range(26):
        index = (num_key + i) % 26
        if index == 0:
            index = 26
        cycle.append(index)
    num_rotor = cycle[rotor]
    print(cycle)

    return(num_rotor)

def letter_output(rotor3):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for i in range (26):
        if alphabet[i] == rotor3:
            num_letter = i
    return (alphabet[num_letter])

# method = input("Choose your input method (default/textfile): ")
# while len(method) == 0:
#     print("Input method cannot be empty!")
#     method = input("Choose your input method (default/textfile): ")
# while method != 'default' and method != 'textfile':
#     print("Please choose default or grouped method!")
#     method = input("Choose your input method (default/textfile): ")

plaintext = input("Enter your plaintext: ").lower()
while len(plaintext) == 0:
        print("Output method cannot be empty!")
        plaintext = input("Enter your plaintext: ").lower()

key = input("Enter your key: ").lower()
while len(key) == 0:
    print("Output method cannot be empty!")
    key = input("Enter your key: ").lower()
while len(key) != 3:
    print("Please enter 3 letters!")
    key = input("Enter your key: ").lower()

listkey = list(key)

rotor1 = letter(plaintext) #1
for i in range(len(rotor1)):
    cycle1 = search(rotor1[i], listkey[0]) #25
    print(cycle1)
    rotor2 = slow_rotor(cycle1) #25
    print(rotor2)
    cycle2 = search (rotor2, listkey[1]) #22
    print(cycle2)
    rotor3 = medium_rotor(cycle2) #22
    print(rotor3)
    cycle3 = search (rotor3, listkey[2]) #13
    print(cycle3)
    rotor4 = fast_rotor(cycle3) #13 -> i
    print(rotor4)
    listkey[2] = chr(ord(listkey[2]) + 1)
    # fast_list = majuin yang paling belakang gimana ya caranya
    print('---')