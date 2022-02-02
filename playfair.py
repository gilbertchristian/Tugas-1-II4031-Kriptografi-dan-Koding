import math


def create_key(key):
    text = ''.join(dict.fromkeys(key))
    text = ''.join(i for i in key if i.isalnum())

    key = list(set('abcdefghiklmnopqrstuvwxyz') - set(text))
    key.sort()
    key = ''.join(key)
    return(text + key)


def create_matrix(row, column, full_key):
    matrix = []
    for i in range(row):
        row_list = []
        for j in range(column):
            row_list.append(full_key[row * i + j])
        matrix.append(row_list)
        print(row_list)


def abc(plaintext, key):
    for letter in plaintext:
        if letter == 'j':
            plaintext = plaintext.replace('j', 'i')

    # MISAHIN JADI BIGRAM
    # plaintext = list(plaintext)
    # num = math.ceil(int(len(plaintext)/2))
    # bigram_plaintext = []
    # for i in range(num):
    #     bigram = []
    #     for j in range(2):
    #         bigram.append(plaintext[2 * i + j])
    #     bigram_plaintext.append(bigram)
    # print(bigram_plaintext)

    return(plaintext)


plaintext = input("Enter your plaintext: ").lower()
key = input("Enter your key: ").lower()
full_key = create_key(key)
create_matrix(5, 5, full_key)
abc(plaintext, full_key)
