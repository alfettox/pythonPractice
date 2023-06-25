# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 08:28:04 2023

@author: Giovanni De Francschi

""" 


#Count words

def read_text_file():
    with open('data.txt', 'r') as file:
        text = file.read()
    return text

read_text_file()
print(text)
