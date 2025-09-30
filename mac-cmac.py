import base64
import os
from cryptography.hazmat.primitives import cmac
from cryptography.hazmat.primitives.ciphers import algorithms
from cryptography.exceptions import InvalidSignature

#1. CMAC 생성 (송신자)
key = os.urandom(16) 
message = 'Message to authenticate 메시지인증코드 테스트'
c = cmac.CMAC(algorithms.AES(key))
c.update(message.encode('utf-8'))
signature = c.finalize()
print('Key: ',base64.b64encode(key).decode())
print('Key(hex): ',key.hex())
print('Message: ', message)
print('Signature: ',signature.hex())

# 송신자 -> 수신자 검증 (message, signature) 검증

#2. CMAC 검증 (수신자)
try:
	c = cmac.CMAC(algorithms.AES(key))
	c.update(message.encode('utf-8'))
	c.verify(signature)
	print("검증 성공")
except InvalidSignature:
	print("\n검증 실패: 서명이 유효하지 않습니다.")
