import math


def create_key(key):
    text = ''.join(dict.fromkeys(key))
    text = ''.join(i for i in key if i.isalnum())

    key = list(set('abcdefghiklmnopqrstuvwxyz') - set(text))
    key.sort()
    key = ''.join(key)
    return(text + key)


def filter(plaintext):
    remove_punctuation_space = ''.join(i for i in plaintext if i.isalnum())
    remove_number = ''.join(
        i for i in remove_punctuation_space if not i.isdigit())
    return(remove_number)


def create_matrix(key):
    matrix = []
    for i in range(5):
        row_list = []
        for j in range(5):
            row_list.append(full_key[5 * i + j])
        matrix.append(row_list)
        print(row_list)
    return(matrix)


def arrange(plaintext, key):
    for letter in plaintext:
        if letter == 'j':
            plaintext = plaintext.replace('j', 'i')

    plaintext = list(plaintext)

    curr = ''
    foll = ''
    i = 0
    while i != len(plaintext)-1:
        curr = plaintext[i]
        foll = plaintext[i+1]
        if curr == foll:
            plaintext.insert(i+1, 'x')
        i += 1

    if len(plaintext) % 2 == 1:
        plaintext.append('x')

    bigram_plaintext = []
    for i in range(int(len(plaintext)/2)):
        bigram = []
        for j in range(2):
            bigram.append(plaintext[2 * i + j])
        bigram_plaintext.append(bigram)
    return(bigram_plaintext)


def encrypt(plaintext, key):
    ciphertext = []
    plaintext = list(plaintext)

    for i in range(len(plaintext)):
        curr = search(plaintext[i][0], plaintext[i][1], key)

        x1 = curr[0][1]
        y1 = curr[0][0]
        x2 = curr[1][1]
        y2 = curr[1][0]

        if y1 == y2:
            new_x1 = (x1+1) % 5
            new_x2 = (x2+1) % 5
            ciphertext.append(get(y1, new_x1, key))
            ciphertext.append(get(y2, new_x2, key))
        elif x1 == x2:
            new_y1 = (y1+1) % 5
            new_y2 = (y2+1) % 5
            ciphertext.append(get(new_y1, x1, key))
            ciphertext.append(get(new_y2, x2, key))
        else:
            ciphertext.append(get(y1, x2, key))
            ciphertext.append(get(y2, x1, key))

    ciphertext = ''.join(ciphertext)
    return(ciphertext)


def search(letter1, letter2, key):
    for i in range(5):
        for j in range(5):
            if key[i][j] == letter1:
                pos1 = [i, j]
            elif key[i][j] == letter2:
                pos2 = [i, j]
    return(pos1, pos2)


def get(pos1, pos2, key):
    for i in range(5):
        for j in range(5):
            if i == pos1 and j == pos2:
                return(key[i][j])


plaintext = input("Enter your plaintext: ").lower()
key = input("Enter your key: ").lower()

filtered_plaintext = filter(plaintext)
full_key = create_key(key)
matrix_key = create_matrix(full_key)
arranged_plaintext = arrange(filtered_plaintext, matrix_key)
encrypted_text = encrypt(arranged_plaintext, matrix_key)

print("Ciphertext:", encrypted_text)
