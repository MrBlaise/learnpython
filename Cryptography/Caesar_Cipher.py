#!/usr/bin/env python3
""" A program to use a Caesar cipher based on user input for the shift value """

MAX_SHIFT = 26

def what_mode():
    """ Finds out what the user wants to do """
    while True:
        print("Do you wish to encrypt,  decrypt or brute force a message: ")
        mode = input().lower()
        if mode in "encrypt e decrypt d brute b".split():
            return mode[0]
        else:
            print("Enter '[E]ncrypt',  '[D]ecrypt' or [B]rute")

def plain_message():
    """ Gets a string from the user """
    print ("Message: ")
    return input()

def get_key():
    """ Gets a shift value from the user """
    shift_key = 0
    while True:
        print("Enter shift key (1-%s) " % (MAX_SHIFT))
        shift_key = int(input())
        if (shift_key >= 1 and shift_key <= MAX_SHIFT):
            return shift_key

def crypt_message(mode, message, shift_key):
    """ The encryption / decryption action is here """
    if mode[0] == 'd':
        shift_key = -shift_key
    translated = ''

    for symbol in message: # The encryption stuff
        if symbol.isalpha():
            num = ord(symbol)
            num += shift_key

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

mode = what_mode()
message = plain_message()

if mode[0] != 'b':
    shift_key = get_key()

print('Your translated text is:')

if mode[0] != 'b': #Brute force settings
    print(crypt_message(mode, message, shift_key))
else:
    for shift_key in range(1, MAX_SHIFT + 1):
        print(shift_key, crypt_message('decrypt', message, shift_key))
