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

    string_key = ''.join(key)
    return(string_key)


def encrypt(plaintext, key):
    ciphertext = []

    for i in range(len(plaintext)):
        number_plaintext = ord(plaintext[i]) - ord('a')
        number_key = ord(key[i]) - ord('a')
        number_ciphertext = (number_plaintext + number_key) % 26
        ciphertext.append(chr(number_ciphertext + ord('a')))

    string_ciphertext = ''.join(ciphertext)
    return(string_ciphertext)


def decrypt(ciphertext, key):
    plaintext = []

    for i in range(len(ciphertext)):
        number_ciphertext = ord(ciphertext[i]) - ord('a')
        number_key = ord(key[i]) - ord('a')
        number_plaintext = (number_ciphertext - number_key) % 26
        plaintext.append(chr(number_plaintext + ord('a')))
    string_plaintext = ''.join(plaintext)
    return(string_plaintext)


plaintext = input("Enter your plaintext: ").lower()
key = input("Enter your key: ").lower()

filterd_plaintext = filter(plaintext)
extended_key = extend_key(filterd_plaintext, key)
encrypted_text = encrypt(filterd_plaintext, extended_key)
decrypted_text = decrypt(encrypted_text, extended_key)

print("Ciphertext:", encrypted_text)
print("Decrypted ciphertext:", decrypted_text)
