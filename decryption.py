#!/usr/bin/env python
#_*_ coding:utf-8 _*_
from encryption import *

def de_change(ch,num):
    """
    de_change函数的作用是根据密文字符和密钥还原明文字符
    :param ch: 密文字符
    :param num: 密钥编码
    :return: 明文字符
    """
    ch_num = char_to_num(ch)
    result = ch_num - num
    if result < 0:
        result = 26 + result
    return result

def decrypt(key):
    """
    decryption函数的主要作用是将密文解密成明文
    :param key: 密钥
    :return: 明文
    """
    with open('crypt.txt','r') as f:
        ciphertext = f.read()
    num_key = key_to_num(key)
    wen = ''
    k = 0
    for c in ciphertext:
        if k == len(num_key):
            k = 0
        w = de_change(c,num_key[k])
        w = num_to_char(w)
        wen = wen + w
        k += 1
    wirte_txt(wen,'result.txt')
    return wen