import string

def generate_matrix(keyword: str):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    keyword = keyword.upper().replace("J", "I")
    matrix = []
    for char in keyword:
        if char not in matrix and char in alphabet:
            matrix.append(char)
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
    return [matrix[i*5:(i+1)*5] for i in range(5)]

def preprocess_text(text: str):
    text = text.upper().replace("J", "I")
    result = ""
    i = 0
    while i < len(text):
        a = text[i]
        if i+1 < len(text):
            b = text[i+1]
            if a == b:
                result += a + "X"
                i += 1
            else:
                result += a + b
                i += 2
        else:
            result += a + "X"
            i += 1
    return result

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def encrypt_pair(pair, matrix):
    a, b = pair
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)
    if row1 == row2:  
        return matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
    elif col1 == col2:  
        return matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
    else:  
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt_pair(pair, matrix):
    a, b = pair
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)
    if row1 == row2:  
        return matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5]
    elif col1 == col2:  
        return matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2]
    else:  
        return matrix[row1][col2] + matrix[row2][col1]

def encrypt(text, keyword):
    matrix = generate_matrix(keyword)
    text = preprocess_text(text)
    ciphertext = ""
    for i in range(0, len(text), 2):
        ciphertext += encrypt_pair(text[i:i+2], matrix)
    return ciphertext

def decrypt(text, keyword):
    matrix = generate_matrix(keyword)
    plaintext = ""
    for i in range(0, len(text), 2):
        plaintext += decrypt_pair(text[i:i+2], matrix)
    return plaintext

# 실행 예시
keyword = "SECRET"
plain = "HELLO"
cipher = encrypt(plain, keyword)
decoded = decrypt(cipher, keyword)

print("키워드:", keyword)
print("평문:", plain)
print("암호문:", cipher)
print("복호화 결과:", decoded)
