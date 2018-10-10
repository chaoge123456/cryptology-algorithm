#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import msvcrt,sys
from encryption import encrypt
from decryption import decrypt
import getpass

if __name__ == "__main__":
    print("**************************************************************************")
    print("*                                                                        *")
    print("*                      维吉尼亚加解密算法演示                            *")
    print("*                                                                        *")
    print("**************************************************************************")
    flag = True
    while flag:
        print("\n请选择您要进行的操作：1.加密(按E键) 2.解密(按D键） 3.退出(任意键)\n")
        u = input("您选择的操作是：")
        if u == "E":
            print("(温馨提示：进行加密前请清空plain.txt文件中的内容，并将明文复制到该文件中)")
            key = getpass.getpass("请输入加密密钥:")
            encrypt(key)
            print("加密完成，请到crypt.txt文件中查看密文")
        elif u == "D":
            print("(温馨提示：进行解密前请清空crypt.txt文件中的内容，并将密文复制到该文件中)")
            key = getpass.getpass("请输入解密密钥:")
            decrypt(key)
            print("解密完成，请到result.txt文件中查看明文")
        else:
            flag = False

