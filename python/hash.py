import hashlib

# md5
text = 'test'
print(hashlib.md5(text.encode('utf-8')).hexdigest())

# SHA-1
print(hashlib.sha1(text.encode()).hexdigest())

# SHA-224
print(hashlib.sha224(text.encode()).hexdigest())

# SHA-256
print(hashlib.sha256(text.encode()).hexdigest())

# SHA-384
print(hashlib.sha384(text.encode()).hexdigest())

# SHA-512
print(hashlib.sha512(text.encode()).hexdigest())

# BASE16
import base64
text = 'test'.encode('ascii')
print(base64.b16encode(text).decode('ascii'))

text = 'dGVzdA=='
print(base64.b16decode(text).decode('ascii'))

# BASE32
import base64
text = 'test'.encode('ascii')
print(base64.b32encode(text).decode('ascii'))

text = 'dGVzdA=='
print(base64.b32decode(text).decode('ascii'))

# BASE64
import base64
text = 'test'.encode('ascii')
print(base64.b64encode(text).decode('ascii'))

text = 'dGVzdA=='
print(base64.b64decode(text).decode('ascii'))