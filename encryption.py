#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import re

s = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def pretreatment():
    """
    pretreatment函数的主要作用是对明文进行预处理，去除非字母字符和转换大小写
    :return: 经过预处理的明文字符串
    """
    with open("plain.txt","r") as f:
        wen = f.read()
    pattern = re.compile('[\n]|\d|\W')
    plain_1 = re.sub(pattern,'',wen).lower()
    return plain_1

def wirte_txt(txt,filename):
    """
    write函数的主要作用是将字符串写入txt文件中
    :param txt: 字符串
    :param filename: 文件名
    :return:
    """
    with open(filename,"w") as f:
        f.write(txt)

def char_to_num(ch):
    """
    char_to_num将字符转换为数字编码
    :param ch: 字符
    :return: 返回对应的数字编码
    """
    num = s.index(ch)
    return num

def num_to_char(num):
    """
    num_to_char函数的主要作用是将数字编码还原为对于的字符
    :param num: 数字编码
    :return: 返回对于的字符
    """
    return s[num]

def key_to_num(key):
    """
    key_to_num函数的主要作用是将密钥转换为数字编码列表
    :param key: 密钥
    :return: 密钥的编码列表
    """
    num_key = []
    for i in key:
        num = char_to_num(i)
        num_key.append(num)
    return num_key

def change(ch,num):
    """
    change函数的主要作用是将明文字符与密钥编码进行取余
    :param ch: 明文字符
    :param num: 密钥编码
    :return: 密文字符
    """
    ch_num = char_to_num(ch)
    result = (ch_num + num) % 26
    return result

def encrypt(key):
    """
    encrypt函数的主要作用是进行加密
    :param key: 密钥
    :return: 密文字符串
    """
    wen = pretreatment()
    num_key = key_to_num(key)
    ciphertext = ''
    k = 0
    for w in wen:
        if k == len(num_key):
            k = 0
        cipher = change(w,num_key[k])
        cipher = num_to_char(cipher)
        ciphertext = ciphertext + cipher
        k += 1
    wirte_txt(ciphertext,'crypt.txt')
    return ciphertext

