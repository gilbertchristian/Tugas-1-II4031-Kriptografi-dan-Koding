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


def create_matrix(row, column, full_key):
    matrix = []
    for i in range(row):
        row_list = []
        for j in range(column):
            row_list.append(full_key[row * i + j])
        matrix.append(row_list)
        print(row_list)


def arrange_plaintext(plaintext, key):
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
    print(bigram_plaintext)

    return(plaintext)

# def encrypt(plaintext, key):
#     for i in range(plaintext):
#         for j in range(2):

def search(plaintext, key):
    for i in range 


plaintext = input("Enter your plaintext: ").lower()
key = input("Enter your key: ").lower()

filtered_plaintext = filter(plaintext)
full_key = create_key(key)

create_matrix(5, 5, full_key)
arrange_plaintext(plaintext, key)(filtered_plaintext, full_key)
