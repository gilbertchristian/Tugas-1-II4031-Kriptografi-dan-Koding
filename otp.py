import random

character = "abcdefghijklmnopqrstuvwxyz"

def encrypt(plaintext):
    otp = "".join(random.sample(character, len(plaintext)))
    final = []

    listplain = list(plaintext)
    listotp = list(otp)

    for i in range(len(plaintext)):
        output = (number(listplain[i])+number(listotp[i])) % 26
        result = letter(output)
        final.append(result)

    end = "".join(final)
    return otp, end

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

plaintext = input("Enter your plaintext: ").lower()
encrypted = encrypt(plaintext)
decrypted = decrypt(encrypted[1], encrypted[0])


print("OTP: " + encrypted[0])
print("Encrypted: " + encrypted[1])
print("Decrypted: " + decrypted)

