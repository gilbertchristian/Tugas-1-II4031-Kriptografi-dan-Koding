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
    print (otp)
    print (end)
    return otp, end


def number(letter):
    return(ord(letter) - 96)

def letter(number):
    return(chr(number + 96))

plaintext = input("Enter your plaintext: ").lower()
encrypted = encrypt(plaintext)


print("OTP: " + encrypted[0])
print("Encrypted: " + encrypted[1])

