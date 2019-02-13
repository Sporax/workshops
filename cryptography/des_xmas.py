from Crypto.Cipher import DES

# create new DES instance
key = '0101010101010101'.decode('hex')
iv = '0000000000000000'.decode('hex')
des = DES.new(key, DES.MODE_CBC, iv)

# TODO: double check len(m) div by 8
m = b'xxx Redacted xxx'
c = des.encrypt(m)

c = c.encode('hex')
f = open('des_out.enc', 'w')
f.write('c = ', c)
f.close()
