from itertools import cycle

slow_list = [21, 3, 15, 1, 19, 10, 14, 26, 20, 8, 16,
            7, 22, 4, 11, 5, 17, 9, 12, 23, 18, 2, 25, 6, 24, 13]
medium_list = [20, 1, 6, 4, 15, 3, 14, 12, 23, 5, 16, 2,
            22, 19, 11, 18, 25, 24, 13, 7, 10, 8, 21, 9, 26, 17] 
fast_list = [8, 18, 26, 17, 20, 22, 10, 3, 13, 11, 4,
            23, 5, 24, 9, 12, 25, 16, 19, 6, 15, 21, 2, 7, 1, 4]    

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
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for i in range (26):
        if alphabet[i] == plaintext:
            num_letter = i
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
    
plaintext = input("Enter your plaintext: ").lower()
key1 = input("Enter your key: ").lower()
rotor1 = letter(plaintext)
cycle1 = search(rotor1, key1)
print('cycle1', cycle1)

key2 = input("Enter your key: ").lower()
rotor2 = slow_rotor(cycle1)
print('rotor1',rotor2)

cycle2 = search (rotor2, key2)
print('cycle2',cycle2)

key3 = input("Enter your key: ").lower()
rotor3 = medium_rotor(cycle2)
print('rotor2',rotor3)

cycle3 = search (rotor3, key3)
print('cycle3',cycle3)

rotor4 = fast_rotor(cycle3)
print('rotor3',rotor4)