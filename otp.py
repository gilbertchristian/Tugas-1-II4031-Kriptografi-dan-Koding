import random


def OneTimePad_key(plaintext):
    character = "abcdefghijklmnopqrstuvwxyz"
    return ("".join(random.sample(character, len(plaintext))))


def filter(text):
    remove_punctuation_space = ''.join(i for i in text if i.isalnum())
    remove_number = ''.join(
        i for i in remove_punctuation_space if not i.isdigit())
    return(remove_number)


def encrypt(plaintext, otp):
    final = []

    listplain = list(plaintext)
    listotp = list(otp)

    for i in range(len(plaintext)):
        output = (number(listplain[i])+number(listotp[i])) % 26
        result = letter(output)
        final.append(result)

    end = "".join(final)
    return end


def decrypt(ciphertext, otp):
    final = []
    listcipher = list(ciphertext)
    listotp = list(otp)

    for i in range(len(ciphertext)):
        output = (number(listcipher[i]) - number(listotp[i])) % 26
        result = letter(output)
        final.append(result)

    end = "".join(final)
    return end


def number(letter):
    return(ord(letter) - 97)


def letter(number):
    return(chr(number + 97))


def group(ciphertext):
    output = []
    ciphertext = list(ciphertext)

    for i in range(len(ciphertext)):
        if i % 5 == 0 and i > 0:
            output.append(' ')
        output.append(ciphertext[i])

    output = ''.join(output)
    return(output)


# plaintext = input("Enter your plaintext: ").lower()
# encrypted = encrypt(plaintext)
# decrypted = decrypt(encrypted[1], encrypted[0])


# print("OTP: " + encrypted[0])
# print("Encrypted: " + encrypted[1])
# print("Decrypted: " + decrypted)


def OneTimePad_Process(plaintext, key):
    plaintext = filter(plaintext)
    encrypted_text = encrypt(plaintext, key)
    grouped_encrypted_text = group(encrypted_text)
    decrypted_text = decrypt(encrypted_text, key)
    return(encrypted_text, grouped_encrypted_text, decrypted_text, key)


def OneTimePad_Export(plaintext, key):
    cipher = OneTimePad_Process(plaintext, key)
    txt = open('ciphertext.txt', 'w')
    cipher = txt.write(cipher[0])
    txt.close()
