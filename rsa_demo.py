import rsa


data = 'this data needs to be encrypted'
public_key, private_key = rsa.newkeys(512)

encrypted_data = rsa.encrypt(data.encode('utf8'), public_key)
print(encrypted_data)

content = rsa.decrypt(encrypted_data, private_key)
print(content.decode('utf8'))
