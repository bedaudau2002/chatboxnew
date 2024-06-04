from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

import os
import requests

def keyGenRSA():
    key_pair = RSA.generate(1024)

    public_key = key_pair.publickey().exportKey()
    private_key = key_pair.exportKey()

    print(public_key)
    print(private_key)

    # Save private key to private folder
    private_key_path = '/home/bedaudau/Desktop/chatboxnew/private/privateRSA_key.pem'
    with open(private_key_path, 'wb') as f:
        f.write(private_key)
        f.close()
    print(f"Private key saved to {private_key_path}")
    # Save public key to public folder
    public_key_path = '/home/bedaudau/Desktop/chatboxnew/public/publicRSA_key.pem'
    with open(public_key_path, 'wb') as f:
        f.write(public_key)
        f.close()
    print(f"Public key saved to {public_key_path}")


#keyGenRSA()

def getPublicRSAKey():
    public_key_path = '/home/bedaudau/Desktop/chatboxnew/public/publicRSA_key.pem'
    with open(public_key_path, 'rb') as f:
        public_key = f.read()
        f.close()
    return public_key

def getPrivateRSAKey():
    private_key_path = '/home/bedaudau/Desktop/chatboxnew/private/privateRSA_key.pem'
    with open(private_key_path, 'rb') as f:
        private_key = f.read()
        f.close()
    return private_key

#session key creation and encryption
def encryptMessage(message):
    recipient_key = RSA.import_key(getPublicRSAKey())
    session_key = get_random_bytes(16)

    # Encrypt the session key with the public RSA key

    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    # Encrypt the data with the AES session key

    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(message)

    return enc_session_key, cipher_aes.nonce, tag, ciphertext

#cipher RSA and session key decryption
def decryptMessage(enc_session_key, nonce, tag, ciphertext):
    private_key = getPrivateRSAKey()
    recipient_key = RSA.import_key(private_key)

    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    session_key = cipher_rsa.decrypt(enc_session_key)

    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)

    return data

# keyGenRSA()
# data = encryptMessage('Hello World')
# print(data)
# print()
# print(data[0])
# print()
# print(data[1])
# print()
# print(data[2])
# print()
# print(data[3])
# print()
# print(decryptMessage(data[0], data[1], data[2], data[3]))
