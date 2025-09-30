from cryptography.hazmat.primitives import hashes

message = 'hash test. 해시함수 테스트...'
print("Message:", message) 

#1. SHA1 해시 계산
digest = hashes.Hash(hashes.SHA1())
digest.update(message.encode('utf-8'))
hash_value = digest.finalize() 
print("SHA1 해시(hex):", hash_value.hex())

#2. SHA256 해시 계산
digest = hashes.Hash(hashes.SHA256())
digest.update(message.encode('utf-8'))
hash_value = digest.finalize() 
print("SHA-256 해시(hex):", hash_value.hex())

#3. SHA512 해시 계산
digest = hashes.Hash(hashes.SHA512())
digest.update(message.encode('utf-8'))
hash_value = digest.finalize() 
print("SHA-512 해시(hex):", hash_value.hex())

#4. SHA3_384 해시 계산
digest = hashes.Hash(hashes.SHA3_384())
digest.update(message.encode('utf-8'))
hash_value = digest.finalize() 
print("SHA3_384 해시(hex):", hash_value.hex())

#5. BLAKE2b 해시 계산
digest = hashes.Hash(hashes.BLAKE2b(64))
digest.update(message.encode('utf-8'))
hash_value = digest.finalize() 
print("BLAKE2b(64) 해시(hex):", hash_value.hex())
