#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import rsa

def makeKey():
    (pubkey, privkey) = rsa.newkeys(1024)
    with open('public.pem', 'w+') as f:
        f.write(pubkey.save_pkcs1().decode())
    with open('private.pem', 'w+') as f:
        f.write(privkey.save_pkcs1().decode())
    print('秘钥生成成功')

def readKey(name):
    if name == 'public' or name == 'private':
        with open(name+'.pem', 'r') as f:
            return f.read().encode()

def encrypt(text):
    pubkey = rsa.PublicKey.load_pkcs1(readKey('public'))
    res = rsa.encrypt(text.encode(), pubkey)
    print(res.decode())
    return res
def decrypt():
    enCode = encrypt('gaona')
    print(enCode)
    privkey = rsa.PrivateKey.load_pkcs1(readKey('private'))
    res = rsa.decrypt(enCode, privkey).decode()
    print(res)

#makeKey()
decrypt()
