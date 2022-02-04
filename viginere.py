def filter(plaintext):
    remove_punctuation_space = ''.join(i for i in plaintext if i.isalnum())
    remove_number = ''.join(
        i for i in remove_punctuation_space if not i.isdigit())
    return(remove_number)


def extend_key(plaintext, key):
    key = list(key)
    key_length = len(key)
    if len(key) == len(plaintext):
        return key
    else:
        for i in range(len(key), len(plaintext)):
            key.append(key[i % key_length])

    key = ''.join(key)
    return(key)


def encrypt(plaintext, key):
    ciphertext = []

    for i in range(len(plaintext)):
        number_plaintext = ord(plaintext[i]) - ord('a')
        number_key = ord(key[i]) - ord('a')
        number_ciphertext = (number_plaintext + number_key) % 26
        ciphertext.append(chr(number_ciphertext + ord('a')))

    ciphertext = ''.join(ciphertext)
    return(ciphertext)


def decrypt(ciphertext, key):
    plaintext = []

    for i in range(len(ciphertext)):
        number_ciphertext = ord(ciphertext[i]) - ord('a')
        number_key = ord(key[i]) - ord('a')
        number_plaintext = (number_ciphertext - number_key) % 26
        plaintext.append(chr(number_plaintext + ord('a')))
    plaintext = ''.join(plaintext)
    return(plaintext)


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

# if method == 'default':
#     plaintext = input("Enter your plaintext: ").lower()
#     while len(plaintext) == 0:
#         print("Output method cannot be empty!")
#         plaintext = input("Enter your plaintext: ").lower()
# else:
#     with open('plaintext.txt') as text:
#         plaintext = text.readlines()
#     text.close()

# key = input("Enter your key: ").lower()
# while len(key) == 0:
#     print("Output method cannot be empty!")
#     key = input("Enter your key: ").lower()

# output = input("Choose your output method (default/grouped): ")
# while len(output) == 0:
#     print("Output method cannot be empty!")
#     output = input("Choose your output method (default/grouped): ")
# while output != 'default' and output != 'grouped':
#     print("Please choose default or grouped method!")
#     output = input("Choose your output method (default/grouped): ")

# filtered_plaintext = filter(plaintext)
# filtered_key = filter(key)
# extended_key = extend_key(filtered_plaintext, filtered_key)

# encrypted_text = encrypt(filtered_plaintext, extended_key)
# grouped_encrypted_text = group(encrypted_text)

# decrypted_text = decrypt(encrypted_text, extended_key)

# if output == 'default':
#     print("Ciphertext:", encrypted_text)
# else:
#     print("Ciphertext:", grouped_encrypted_text)

# print("Decrypted ciphertext:", decrypted_text)


def Viginere_Process(plaintext, key):
    filtered_plaintext = filter(plaintext)
    filtered_key = filter(key)
    extended_key = extend_key(filtered_plaintext, filtered_key)
    encrypted_text = encrypt(filtered_plaintext, extended_key)
    grouped_encrypted_text = group(encrypted_text)
    decrypted_text = decrypt(encrypted_text, extended_key)
    return(encrypted_text, grouped_encrypted_text, decrypted_text)


def Viginere_Export(plaintext, key):
    cipher = Viginere_Process(plaintext, key)
    txt = open('ciphertext.txt', 'w')
    cipher = txt.write(cipher[0])
    txt.close()
