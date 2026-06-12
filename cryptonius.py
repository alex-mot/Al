#!/usr/bin/env python3
"""
cryptonius.py
Contains encryption/decryption utilities for DigiCore Password Manager.
"""

CHARSET = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\\}]{["\':;?/>.<, '


def rot3_encrypt(text):
    """
    Encrypt text using ROT3-style shift over the custom CHARSET.
    (Preserves characters not present in CHARSET.)
    """
    encrypted = []
    for char in text:
        if char in CHARSET:
            index = CHARSET.find(char)
            encrypted.append(CHARSET[(index + 5) % len(CHARSET)])
        else:
            encrypted.append(char)
    return ''.join(encrypted)


def rot3_decrypt(text):
    """
    Decrypt text encrypted with `rot3_encrypt` above.
    """
    decrypted = []
    for char in text:
        if char in CHARSET:
            index = CHARSET.find(char)
            decrypted.append(CHARSET[(index - 5) % len(CHARSET)])
        else:
            decrypted.append(char)
    return ''.join(decrypted)
