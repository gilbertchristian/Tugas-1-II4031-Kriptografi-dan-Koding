from itertools import cycle

slow_list = [1, 19, 10, 14, 26, 20, 8, 16,
            7, 22, 4, 11, 5, 17, 9, 12, 23, 18, 2, 25, 6, 24, 13, 21, 3, 15]
medium_list = [1, 6, 4, 15, 3, 14, 12, 23, 5, 16, 2,
            22, 19, 11, 18, 25, 24, 13, 7, 10, 8, 21, 9, 26, 17,20] 
fast_list = [8, 18, 26, 17, 20, 22, 10, 3, 13, 11, 4,
            23, 5, 24, 9, 12, 25, 16, 19, 6, 15, 21, 2, 7, 1, 14]    

def set_list(key, letter):
    pos = number(letter)
    for i in  range(pos-1):
        rotate(key)
        

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

def number_plaintext(plaintext):
    num_letter = []
    
    for letter in plaintext:
        num_letter.append(number(letter) - 1)
        
    print(num_letter)
    return (num_letter) #bb -> 1,1

def search(pos, key):
    list = list_key(key)
    for i in range(26):
        if list[i] == pos:
            return(pos+1)

def list_key(key):
    list = []

    for i in range(26):
        index = (number(key) + i) % 26

        if index == 0:
            index = 26
        list.append(index)
    print(list)
    return(list)

def letter_output(rotor3):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for i in range (26):
        if alphabet[i] == rotor3:
            num_letter = i
    return (alphabet[num_letter])

def number(letter):
    return(ord(letter)-96)

def letter(number):
    return(chr(number+96))

def cycle(letter):
    cycle1 = search(letter, key[0]) #25  search(1,x)
    print(cycle1)
    rotor1 = slow_rotor(cycle1) #25
    print(rotor1)
    cycle2 = search(rotor1, key[1]) #22 
    print(cycle2)
    rotor2 = medium_rotor(cycle2) #22
    print(rotor2)
    cycle3 = search(rotor2, key[2]) #13
    print(cycle3)
    rotor3 = fast_rotor(cycle3) #13 -> i
    print(rotor3)
    return(rotor3)

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

key = list(key)

plaintext = number_plaintext(plaintext) #1
ciphertext =[]

set_list(slow_list,key[0])
set_list(medium_list,key[1])
set_list(fast_list,key[2])

for i in range(len(plaintext)): #b, b
    ciphertext.append(cycle(plaintext[i]))
    #x, z ,a -> x, z, b
    if number(key[2]) < 26:
        key[2] = letter(number(key[2]) + 1)
        rotate(fast_list)
    elif number(key[2]) == 26:
        key[2] = 'a'
        key[1] = letter(number(key[1]) + 1)
        rotate(fast_list)
        rotate(medium_list)
    elif number(key[2] == 26) and number(key[1]==26):
        key[2] = 'a'
        key[1] = 'a'
        key[0] = letter(number(key[0]) + 1)
        rotate(fast_list)
        rotate(medium_list)
        rotate(slow_list)
    # fast_list = majuin yang paling belakang gimana ya caranya
    print('---')

ciphertext= ''.join(ciphertext)
print(ciphertext)