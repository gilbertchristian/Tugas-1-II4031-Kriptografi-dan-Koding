def create_key(key):
    text = ''.join(i for i in key if i.isalnum())
    text = ''.join(dict.fromkeys(key))

    for letter in text:
        if letter == 'j':
            text = text.replace('j', '')

    key = list(set('abcdefghiklmnopqrstuvwxyz') - set(text))
    key.sort()
    key = ''.join(key)
    return(text + key)


def filter(text):
    remove_punctuation_space = ''.join(i for i in text if i.isalnum())
    remove_number = ''.join(
        i for i in remove_punctuation_space if not i.isdigit())
    return(remove_number)


def create_matrix(key):
    matrix = []
    for i in range(5):
        row_list = []
        for j in range(5):
            row_list.append(key[5 * i + j])
        matrix.append(row_list)
        # print(row_list)
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

    return(bigram(plaintext))


def bigram(plaintext):
    bigram_plaintext = []
    for i in range(int(len(plaintext)/2)):
        bigram = []
        for j in range(2):
            bigram.append(plaintext[2 * i + j])
        bigram_plaintext.append(bigram)
    return(bigram_plaintext)


def encrypt(plaintext, key):
    ciphertext = []
    # plaintext = list(plaintext)

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


def decrypt(ciphertext, key):
    plaintext = []
    ciphertext = list(ciphertext)

    ciphertext = bigram(ciphertext)

    for i in range(len(ciphertext)):
        curr = search(ciphertext[i][0], ciphertext[i][1], key)

        x1 = curr[0][1]
        y1 = curr[0][0]
        x2 = curr[1][1]
        y2 = curr[1][0]

        if y1 == y2:
            new_x1 = (x1-1) % 5
            new_x2 = (x2-1) % 5
            plaintext.append(get(y1, new_x1, key))
            plaintext.append(get(y2, new_x2, key))
        elif x1 == x2:
            new_y1 = (y1-1) % 5
            new_y2 = (y2-1) % 5
            plaintext.append(get(new_y1, x1, key))
            plaintext.append(get(new_y2, x2, key))
        else:
            plaintext.append(get(y1, x2, key))
            plaintext.append(get(y2, x1, key))

    plaintext = ''.join(plaintext)

    for letter in plaintext:
        if letter == 'x':
            plaintext = plaintext.replace('x', '')

    return(plaintext)


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


def group(ciphertext):
    output = []
    ciphertext = list(ciphertext)

    for i in range(len(ciphertext)):
        if i % 5 == 0 and i > 0:
            output.append(' ')
        output.append(ciphertext[i])

    output = ''.join(output)
    return(output)


# plaintext = input("Enter your plaintext: ")
# while len(plaintext) == 0:
#     print("Output method cannot be empty!")
#     plaintext = input("Enter your plaintext: ")

# key = input("Enter your key: ")
# while len(key) == 0:
#     print("Output method cannot be empty!")
#     key = input("Enter your key: ")

# output = input("Choose your output method (default/grouped): ")
# while len(output) == 0:
#     print("Output method cannot be empty!")
#     output = input("Choose your output method (default/grouped): ")
# while output != 'default' and output != 'grouped':
#     print("Please choose default or grouped method!")
#     output = input("Choose your output method (default/grouped): ")

# filtered_plaintext = filter(plaintext)
# filtered_key = filter(key)

# full_key = create_key(filtered_key)
# matrix_key = create_matrix(full_key)
# arranged_plaintext = arrange(filtered_plaintext, matrix_key)
# encrypted_text = encrypt(arranged_plaintext, matrix_key)
# grouped_encrypted_text = group(encrypted_text)
# decrypted_text = decrypt(encrypted_text, matrix_key)

# if output == 'default':
#     print("Ciphertext:", encrypted_text)
# else:
#     print("Ciphertext:", grouped_encrypted_text)

# print("Decrypted ciphertext:", decrypted_text)


def Playfair_Process(plaintext, key):
    filtered_plaintext = filter(plaintext)
    filtered_key = filter(key)

    full_key = create_key(filtered_key)
    matrix_key = create_matrix(full_key)
    arranged_plaintext = arrange(filtered_plaintext, matrix_key)
    encrypted_text = encrypt(arranged_plaintext, matrix_key)
    grouped_encrypted_text = group(encrypted_text)
    decrypted_text = decrypt(encrypted_text, matrix_key)
    return(encrypted_text, grouped_encrypted_text, decrypted_text)
