from pwn import *
import binascii

r = remote('wily-courier.picoctf.net', 59740)
r.recvlines(4); r.recvuntil(b'n: ')
n = int(r.recvline().strip()); r.recvuntil(b'e: ')
e = int(r.recvline().strip()); r.recvuntil(b'ciphertext: ')
c = int(r.recvline().strip())

payload = c * pow(2,e,n)
r.sendlineafter(b'Give me ciphertext to decrypt: ', str(payload))
r.recvuntil(b'Here you go: ')

doubled_plain = int(r.recvline().strip())
print("Doubled Plain:", doubled_plain)
plain_hex = hex(doubled_plain // 2)[2:]
plain_bytes = bytes.fromhex(plain_hex)
print("Plain Text Hex:", plain_hex)
print("Plain Text:", plain_bytes.decode())
r.close()