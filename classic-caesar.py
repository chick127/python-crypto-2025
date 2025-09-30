def caesar_cipher_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if 'a' <= char <= 'z':  
            start = ord('a')
            encrypted_char_code = (ord(char) - start + key) % 26 + start
            encrypted_text += chr(encrypted_char_code)
        elif 'A' <= char <= 'Z':  
            start = ord('A')
            encrypted_char_code = (ord(char) - start + key) % 26 + start
            encrypted_text += chr(encrypted_char_code)
        else:  
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if 'a' <= char <= 'z':
            start = ord('a')
            decrypted_char_code = (ord(char) - start - key) % 26 + start
            decrypted_text += chr(decrypted_char_code)
        elif 'A' <= char <= 'Z':
            start = ord('A')
            decrypted_char_code = (ord(char) - start - key) % 26 + start
            decrypted_text += chr(decrypted_char_code)
        else:
            decrypted_text += char
    return decrypted_text

plaintext = "Hello, Caesar Cipher!"
key = 6

# 암호화
ciphertext = caesar_cipher_encrypt(plaintext, key)
print(f"평문: {plaintext}")
print(f"암호문: {ciphertext}")

# 복호화
decryptedtext = caesar_cipher_decrypt(ciphertext, key)
print(f"복호화평문: {decryptedtext}")


  
