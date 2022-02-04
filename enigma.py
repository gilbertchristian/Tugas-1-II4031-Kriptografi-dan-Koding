from itertools import cycle

slow_list = [1, 19, 10, 14, 26, 20, 8, 16,
             7, 22, 4, 11, 5, 17, 9, 12, 23, 18, 2, 25, 6, 24, 13, 21, 3, 15]
medium_list = [1, 6, 4, 15, 3, 14, 12, 23, 5, 16, 2,
               22, 19, 11, 18, 25, 24, 13, 7, 10, 8, 21, 9, 26, 17, 20]
fast_list = [8, 18, 26, 17, 20, 22, 10, 3, 13, 11, 4,
             23, 5, 24, 9, 12, 25, 16, 19, 6, 15, 21, 2, 7, 1, 14]

slow_list1 = [1, 19, 10, 14, 26, 20, 8, 16,
              7, 22, 4, 11, 5, 17, 9, 12, 23, 18, 2, 25, 6, 24, 13, 21, 3, 15]
medium_list1 = [1, 6, 4, 15, 3, 14, 12, 23, 5, 16, 2,
                22, 19, 11, 18, 25, 24, 13, 7, 10, 8, 21, 9, 26, 17, 20]
fast_list1 = [8, 18, 26, 17, 20, 22, 10, 3, 13, 11, 4,
              23, 5, 24, 9, 12, 25, 16, 19, 6, 15, 21, 2, 7, 1, 14]


def filter(plaintext):
    remove_punctuation_space = ''.join(i for i in plaintext if i.isalnum())
    remove_number = ''.join(
        i for i in remove_punctuation_space if not i.isdigit())
    return(remove_number)


def set_list(key, letter):
    pos = number(letter)
    for i in range(pos-1):
        rotate_forward(key)
    # print(key)


def rotate_forward(list):
    init = list[0]
    i = 0
    while i != len(list)-1:
        list[i] = list[i+1]
        i += 1
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
            return(i)


def key_pos(key, pos):
    lk = list_key(key)
    for i in range(len(lk)):
        if pos == lk[i]:
            return(i)


def number_plaintext(plaintext):
    num_letter = []

    for letter in plaintext:
        num_letter.append(number(letter)-1)

    return (num_letter)  # bb -> 1,1


def search(pos, key):
    key = list_key(key)
    return(key[pos])


def search_rotor(pos, rotor):
    list_rotor = rotor
    for i in range(len(list_rotor)):
        if i == pos:
            return(rotor[i])


def list_key(key):
    list = []

    for i in range(26):
        index = (number(key) + i) % 26

        if index == 0:
            index = 26
        list.append(index)
    # print(list)
    return(list)


def letter_output(rotor3):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for i in range(26):
        if alphabet[i] == rotor3:
            num_letter = i
    return (alphabet[num_letter])


def number(letter):
    return(ord(letter) - 96)


def letter(number):
    return(chr(number + 96))


def cycle_right(let, key):
    cycle1 = search(let, key[0])  # 25  search(1,x)
    rotor1 = slow_rotor(cycle1)  # 25

    cycle2 = search(rotor1, key[1])  # 22
    rotor2 = medium_rotor(cycle2)  # 22

    cycle3 = search(rotor2, key[2])  # 13
    rotor3 = fast_rotor(cycle3)  # 13 -> i
    return(letter(rotor3+1))


def cycle_left(let, key):
    rotor1 = number(let) - 1  # i -> 8

    cycle1 = search_rotor(rotor1, fast_list1)  # 8 -> 13
    fastrot = key_pos(key[2], cycle1)

    rotor2 = search_rotor(fastrot, medium_list1)
    medrot = key_pos(key[1], rotor2)

    rotor3 = search_rotor(medrot, slow_list1)
    slowrot = key_pos(key[0], rotor3)
    return(letter(slowrot+1))


def group(ciphertext):
    output = []
    ciphertext = list(ciphertext)

    for i in range(len(ciphertext)):
        if i % 5 == 0 and i > 0:
            output.append(' ')
        output.append(ciphertext[i])

    output = ''.join(output)
    return(output)

# method = input("Choose your input method (default/textfile): ")
# while len(method) == 0:
#     print("Input method cannot be empty!")
#     method = input("Choose your input method (default/textfile): ")
# while method != 'default' and method != 'textfile':
#     print("Please choose default or grouped method!")
#     method = input("Choose your input method (default/textfile): ")


# plaintext = input("Enter your plaintext: ").lower()
# while len(plaintext) == 0:
#     print("Output method cannot be empty!")
#     plaintext = input("Enter your plaintext: ").lower()

# key = input("Enter your key: ").lower()
# while len(key) == 0:
#     print("Output method cannot be empty!")
#     key = input("Enter your key: ").lower()
# while len(key) != 3:
#     print("Please enter 3 letters!")
#     key = input("Enter your key: ").lower()

# key = list(key)

# plaintext = number_plaintext(plaintext)  # 1
# ciphertext = []

# set_list(slow_list, key[0])
# set_list(medium_list, key[1])
# set_list(fast_list, key[2])

# for i in range(len(plaintext)):  # b, b
#     print(key[0], key[1], key[2])
#     ciphertext.append(cycle(plaintext[i]))

#     # x, z ,a -> x, z, b
#     if number(key[2]) < 26:
#         key[2] = letter((number(key[2]) + 1) % 26)
#         rotate(fast_list)
#     elif number(key[2]) == 26 and number(key[1]) < 26:
#         key[2] = 'a'
#         key[1] = letter((number(key[1]) + 1) % 26)
#         rotate(fast_list)
#         rotate(medium_list)
#     elif number(key[2]) == 26 and number(key[1]) == 26:
#         key[2] = 'a'
#         key[1] = 'a'
#         key[0] = letter((number(key[0]) + 1) % 26)
#         rotate(fast_list)
#         rotate(medium_list)
#         rotate(slow_list)

#     print('---')

# ciphertext = ''.join(ciphertext)
# print(ciphertext)

def encrypt(plaintext, key):
    ciphertext = []
    for i in range(len(plaintext)):
        ciphertext.append(cycle_right(plaintext[i], key))
        if number(key[2]) < 26:  # aaa
            key[2] = letter((number(key[2]) + 1) % 26)
            rotate_forward(fast_list)
        elif number(key[2]) == 26 and number(key[1]) < 26:  # aaz
            key[2] = 'a'
            key[1] = letter((number(key[1]) + 1) % 26)
            rotate_forward(fast_list)
            rotate_forward(medium_list)
        elif number(key[2]) == 26 and number(key[1]) == 26:  # azz
            key[2] = 'a'
            key[1] = 'a'
            key[0] = letter((number(key[0]) + 1) % 26)
            rotate_forward(fast_list)
            rotate_forward(medium_list)
            rotate_forward(slow_list)
    ciphertext = ''.join(ciphertext)
    return(ciphertext)


def decrypt(ciphertext, key):
    ciphertext = list(ciphertext)
    plaintext = []
    for i in range(len(ciphertext)):
        plaintext.append(cycle_left(ciphertext[i], key))
        if number(key[2]) < 26:  # aaa
            key[2] = letter((number(key[2]) + 1) % 26)
            rotate_forward(fast_list1)
        elif number(key[2]) == 26 and number(key[1]) < 26:  # aaz
            key[2] = 'a'
            key[1] = letter((number(key[1]) + 1) % 26)
            rotate_forward(fast_list1)
            rotate_forward(medium_list1)
        elif number(key[2]) == 26 and number(key[1]) == 26:  # azz
            key[2] = 'a'
            key[1] = 'a'
            key[0] = letter((number(key[0]) + 1) % 26)
            rotate_forward(fast_list1)
            rotate_forward(medium_list1)
            rotate_forward(slow_list1)
    plaintext = ''.join(plaintext)
    return(plaintext)


def Enigma_Process(plaintext, key):
    key1 = list(key)
    key2 = list(key)
    plaintext = number_plaintext(filter(plaintext))

    set_list(slow_list, key1[0])
    set_list(medium_list, key1[1])
    set_list(fast_list, key1[2])
    encrypted_text = encrypt(plaintext, key1)

    set_list(slow_list1, key2[0])
    set_list(medium_list1, key2[1])
    set_list(fast_list1, key2[2])
    decrypted_text = decrypt(encrypted_text, key2)

    grouped_encrypted_text = group(encrypted_text)

    return(encrypted_text, grouped_encrypted_text, decrypted_text)


def Enigma_Export(plaintext, key, cipher):
    txt = open('ciphertext.txt', 'w')
    cipher = txt.write(cipher)
    txt.close()
