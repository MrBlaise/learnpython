#!/usr/bin/env python3
""" A program to use a Caesar cipher based on user input for the shift value """

MAX_SHIFT = 26

def whatMode():
    """ Finds out what the user wants to do """
    while True:
        print("Do you wish to encrypt,  decrypt or brute force a message: ")
        mode = input().lower()
        if mode in "encrypt e decrypt d brute b".split():
            return mode[0]
        else:
            print("Enter '[E]ncrypt',  '[D]ecrypt' or [B]rute")

def plainMessage():
    """ Gets a string from the user """
    print ("Message: ")
    return input()

def getKey():
    """ Gets a shift value from the user """
    shiftKey = 0
    while True:
        print("Enter shift key (1-%s) " % (MAX_SHIFT))
        shiftKey = int(input())
        if (shiftKey >= 1 and shiftKey <= MAX_SHIFT):
            return shiftKey

def cryptMessage(mode, message, shiftKey):
    """ The encryption / decryption action is here """
    if mode[0] == 'd':
        shiftKey = -shiftKey
    translated = ''

    for symbol in message: # The encryption stuff
        if symbol.isalpha():
            num = ord(symbol)
            num += shiftKey

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26

            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated

mode = whatMode()
message = plainMessage()

if mode[0] != 'b':
    shiftKey = getKey()

print('Your translated text is:')

if mode[0] != 'b': #Brute force settings
    print(cryptMessage(mode, message, shiftKey))
else:
    for shiftKey in range(1, MAX_SHIFT + 1):
        print(shiftKey, cryptMessage('decrypt', message, shiftKey))
