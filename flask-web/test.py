from cryptography.fernet import Fernet

key = Fernet.generate_key()
f= Fernet(key)
token = f.encrypt(b"secret message.")
print(token)
print(f.decrypt(token))

#암호화 송신자
token = f.encrypt(b"secret message.")

#전송
print(token)

#복호화 수신자
print(f.decrypt(token))

