# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 09:16:05 2023

@author: dottd
"""


#IO READER / WRITER

print("----Simple reader----")

file = open("flatland.txt", "r")
print(file.read())
file.close()

print('\n')
print("----Limit the content----")

file = open("The rise of meritocracy.txt", "r")
print(file.read(200))

file.close()


#Read lines


file = open("The rise of meritocracy.txt", "r")

print(file.readline())
print(file.readline())

print(file.readline())
print(file.readline())

print(file.readline())
print(file.readline())


file.close()


#practice 3
def head(filepath, num_lines):
    with open(filepath, "r") as file:
        lines = file.readlines()
        return "".join(lines[:num_lines])

# Example usage: return the first 5 lines in the file data/text.txt
text = head("The rise of meritocracy.txt", 2)
print(text)


#Iterate

file = open("The rise of Meritocracy.txt");



