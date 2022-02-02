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


def group(ciphertext):
    output = []
    ciphertext = list(ciphertext)

    for i in range(len(ciphertext)):
        if i % 5 == 0 and i > 0:
            output.append(' ')
        output.append(ciphertext[i])

    output = ''.join(output)
    return(output)


plaintext = input("Enter your plaintext: ")
while len(plaintext) == 0:
    print("Output method cannot be empty!")
    plaintext = input("Enter your plaintext: ")

key = input("Enter your key: ")
while len(key) == 0:
    print("Output method cannot be empty!")
    key = input("Enter your key: ")

output = input("Choose your output method (default/grouped): ")
while len(output) == 0:
    print("Output method cannot be empty!")
    output = input("Choose your output method (default/grouped): ")
while output != 'default' and output != 'grouped':
    print("Please choose default or grouped method!")
    output = input("Choose your output method (default/grouped): ")

extended_key = extend_key(plaintext, key)
encrypted_text = encrypt(plaintext, extended_key)
grouped_encrypted_text = group(encrypted_text)
decrypted_text = decrypt(encrypted_text, extended_key)

if output == 'default':
    print("Ciphertext:", encrypted_text)
else:
    print("Ciphertext:", grouped_encrypted_text)

print("Decrypted ciphertext:", decrypted_text)
