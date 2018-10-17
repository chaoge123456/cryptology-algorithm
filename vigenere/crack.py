#!/usr/bin/env python
#_*_ coding:utf-8 _*_
from decryption import de_change

#编码规则
s = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#字母出现频率
frequency = [0.082,0.015,0.028,0.043,0.127,0.022,0.02,0.061,0.07,0.002,0.008,0.04,0.024,0.06,0.075,0.019,0.001,0.06,0.063,0.091,0.028,0.01,0.023,0.001,0.02,0.001]

def count_char(cry,ch):
    """
    count_char函数的主要作用是统计子串中某一字符出现的次数
    :param cry: 子串
    :param ch: 某一字符
    :return: 出现次数
    """
    return cry.count(ch)

def coincidence_index(cry):
    """
    coincidence_index函数的主要作用是计算文本的重合指数
    :param cry: 文本
    :return: 重合指数
    """
    l = len(cry)
    dex = 0.0
    for ch in s:
        num = count_char(cry,ch)
        dex = dex + num*(num-1)/(l*(l-1))
    print("重合指数为：{:.4f}".format(dex))
    return dex

def guess_len_key(crypt):
    """
    guess_len_key函数的主要作用是通过密文猜解密钥长度
    :param crypt: 密文
    :return: 密钥长度以及划为的子串
    """
    l = 1
    d = {}
    while True:
        print("****************************假设密钥长度为%s***********************************" % l)
        sum_index = 0.0
        for i in range(len(crypt)):
            n = i % l
            if n not in d:
                d[n] = ''
            d[n] += crypt[i]
        sum_index = sum(coincidence_index(d[j]) for j in range(l)) / l
        if sum_index >= 0.06 and sum_index <= 0.07:
            break
        else:
            l += 1
            d = {}
    return l,d

def quasi_index(substring,num):
    """
    quasi_index函数的主要作用是计算拟重合指数
    :param substring: 子串
    :param num: num表示具体的哪一个子串
    :return:
    """
    l = len(substring)
    st = ''
    dex = 0.0
    for ch in substring:
        st += s[de_change(ch,num)]
    for i in range(26):
        ch_num = count_char(st,s[i])
        dex += frequency[i] * ch_num / l
    return dex


def crack_key():
    """
    cracker函数的主要作用是破解密钥
    :return: 返回密钥
    """
    with open("crypt.txt","r") as f:
        crypt = f.read()
    len_key,d = guess_len_key(crypt)
    key = ''
    print("\n-------------------------------------")

    print("|       经计算可知，密钥长度为%s         |" % len_key)
    print("-------------------------------------\n")
    for i in range(len_key):
        substring = d[i]
        print("当前字串为：",d[i])
        for n in range(26):
            dex = quasi_index(substring, n)
            print("假设子串移动{},拟重合指数为{:.4f}".format(s[n],dex))
            if dex >= 0.06 and dex <= 0.07:
                key += s[n]
                break
    print("******************************破解的最终密钥为%s*********************************" % key)


