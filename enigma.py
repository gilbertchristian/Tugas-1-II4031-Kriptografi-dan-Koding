def slow_rotor(pos):
    slow_list = [21, 3, 15, 1, 19, 10, 14, 26, 20, 8, 16,
                 7, 22, 4, 11, 5, 17, 9, 12, 23, 18, 2, 25, 6, 24, 13]
    for i in range(len(slow_list)):
        if i == slow_list[i]:
            return(i)


def medium_rotor(pos):
    medium_list = [20, 1, 6, 4, 15, 3, 14, 12, 23, 5, 16, 2,
                   22, 19, 11, 18, 25, 24, 13, 7, 10, 8, 21, 9, 26, 17]
    for i in range(len(medium_list)):
        if i == medium_list[i]:
            return(i)


def fast_rotor(pos):
    fast_list = [8, 18, 26, 17, 20, 22, 10, 3, 13, 11, 4,
                 23, 5, 24, 9, 12, 25, 16, 19, 6, 15, 21, 2, 7, 1, 4]
    for i in range(len(fast_list)):
        if i == fast_list[i]:
            return(fast_list[i])


def cycle(key):
    cycle = []
    alphabet = list('abcdefghiklmnopqrstuvwxyz')
    print(key)
    for i in range(26):
        if alphabet[i] == key:
            num = i + 1
            break
    for i in range(26):
        cycle.append((i + num) % 26)
    return(cycle)


plaintext = input("Enter your plaintext: ").lower()
print(cycle('z'))
