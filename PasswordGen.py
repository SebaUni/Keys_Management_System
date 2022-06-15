import secrets as sr
import string
from numpy import append

_charList = "abcdefghijkmnopkrs"

def Generator(len):
    password= ''.join(sr.choice(_charList) for i in range(len))
    return password

def PasswordsGen(leng):
    passwordList= []
    saved = 0
    while(saved< 10):
        generated= Generator(leng)
        if(leng < 10):
            passwordList.append(generated)
        else:
            if(passwordList.count(generated) == 0):
                passwordList.append(generated)
        saved+=1
    return passwordList

def DisplayPassword(charL):
    global _charList
    _charList= charL
    pwsList= PasswordsGen(10)
    c= 1
    for pws in pwsList:
        print("Password {}: {}".format(c,pws))
        c+=1

DisplayPassword("abcdefghijkmnopkrs123456789")
