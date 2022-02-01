def create_key(key):
    text = ''.join(dict.fromkeys(key))
    text = ''.join(i for i in key if i.isalnum())

    key = list(set('abcdefghiklmnopqrstuvwxyz') - set(text))
    key.sort()
    key = ''.join(key)
    return(text + key)


def create_matrix(row, column, full_key):
    matrix = []
    for i in range(row):
        row_list = []
        for j in range(column):
            row_list.append(full_key[row * i + j])
        matrix.append(row_list)
    print(matrix)


# plaintext = input("Enter your plaintext: ").lower()
key = input("Enter your key: ").lower()
full_key = create_key(key)
create_matrix(5, 5, full_key)
