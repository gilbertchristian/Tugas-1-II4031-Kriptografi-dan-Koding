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
        ciphertext.append(chr(ord(plaintext[i]) + ord(key[i]) % 256))

    ciphertext = ''.join(ciphertext)
    return(ciphertext)


def decrypt(ciphertext, key):
    plaintext = []

    for i in range(len(ciphertext)):
        plaintext.append(chr(ord(ciphertext[i]) - ord(key[i]) % 256))

    plaintext = ''.join(plaintext)
    return(plaintext)


plaintext = input("Enter your plaintext: ").lower()
key = input("Enter your key: ").lower()

extended_key = extend_key(plaintext, key)
encrypted_text = encrypt(plaintext, extended_key)
decrypted_text = decrypt(encrypted_text, extended_key)

print("Ciphertext:", encrypted_text)
print("Decrypted ciphertext:", decrypted_text)
