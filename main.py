def encrypt(plaintext, key):
    ciphertext = []

    for i in range(len(plaintext)):
        number_plaintext = ord(plaintext[i]) - ord('a')
        number_key = ord(key[i]) - ord('a')
        number_ciphertext = (number_plaintext + number_key) % 26
        ciphertext.append(chr(number_ciphertext + ord('a')))

    string_ciphertext = ''.join(map(str, ciphertext))
    return(string_ciphertext)


def extend_key(plaintext, key):
    key = list(key)
    key_length = len(key)
    if len(key) == len(plaintext):
        return key
    else:
        for i in range(len(key), len(plaintext)):
            key.append(key[i % key_length])

    string_key = ''.join(map(str, key))
    return(string_key)


plaintext = input("Enter your plaintext: ")
key = input("Enter your key: ")

extended_key = extend_key(plaintext, key)
encrypted_text = encrypt(plaintext, extended_key)
print("Chipertext:", encrypted_text)
