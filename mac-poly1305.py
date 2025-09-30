import base64
import os
from cryptography.hazmat.primitives import poly1305
from cryptography.exceptions import InvalidSignature
#1. mac 생성 
key = os.urandom(32) 
message = 'Message to authenticate 메시지인증코드 테스트'
p = poly1305.Poly1305(key)
p.update(message.encode('utf-8'))
signature = p.finalize()
print('Key: ',base64.b64encode(key).decode())
print('Message: ', message)
print('mac: ', signature.hex())

# 송신자 -> 수신자 검증 (message, signature) 전송

#2. Poly1305 MAC 검증 (수신자)
try:
    p = poly1305.Poly1305(key)
    p.update(message.encode('utf-8'))
    p.verify(signature)
    print("검증 성공")
except InvalidSignature:
    print("\n검증 실패: 서명이 유효하지 않습니다.")
