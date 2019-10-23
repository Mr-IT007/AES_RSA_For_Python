from Crypto.Cipher import AES
from Crypto import Random
import base64


data = 'this data needs to be encrypted'
key = 'this is a 16 key'.encode('utf8')
iv = Random.new().read(AES.block_size)


def packs7padding(data):
    bs = AES.block_size
    padding = bs - len(data) % bs
    padding_data = chr(padding) * padding

    return data + padding_data


def packs7unpadding(data):
    length = len(data)
    unpadding = ord(data[length - 1])

    return data[: length - unpadding]


def encrypt_aes(data):
    text = packs7padding(data)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(text.encode('utf8'))
    result = base64.b64encode(encrypted).decode('utf8')

    return result


def decrypt_aes(data):
    result = base64.b64decode(data)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(result).decode('utf8')
    result = packs7unpadding(decrypted)

    return result

r = encrypt_aes(data)
print(r)

res = decrypt_aes(r)
print(res)
