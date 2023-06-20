# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 20:48:00 2023

@author: dottd
"""

def display(arg1, *argv):   
    print(arg1)
    if argv:
        for arg in argv:
            print(arg)
 
display("Hello World!", "My name is Haythem Balti.")  # this will execute 
display("Hello World!", "Let's learn Python.", "Let's Python.")  # this will execute
display("Hello World!")  # this will execute
#display()  # this will throw an error because we need at least one argument.


#check frequency of words

def check_words(text, *argv):
    word_frequencies = {}
    lower_text = text.lower()
    words = lower_text.split()
    for word in argv:
        frequency = words.count(word.lower())
        word_frequencies[word] = frequency
    return word_frequencies

text = """The same thing would happen if you were to treat in the same way a Triangle, or Square, 
or any other figure cut out of pasteboard. As soon as you look at it with your eye on the edge on 
the table, you will find that it ceases to appear to you a figure, and that it becomes in appearance 
a straight line. Take for example an equilateral Triangle—who represents with us a Tradesman of 
the respectable class. Fig. 1 represents the Tradesman as you would see him while you were bending 
over him from above; figs. 2 and 3 represent the Tradesman, as you would see him if your eye were 
close to the level, or all but on the level of the table; and if your eye were quite on the level 
of the table (and that is how we see him in Flatland) you would see nothing but a straight line. """

words = check_words(text, "to", "back", "the", "is")
print(words)

words = check_words(text, "over", "level", "way", "square", "figure")
print(words)