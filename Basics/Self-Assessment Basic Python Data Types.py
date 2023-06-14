#!/usr/bin/env python
# coding: utf-8

# In[16]:


#Uppercase and lowercase

fName = input("Please enter your name: ")
fName = fName[0].upper() + fName[1:].lower()
lName = input ("Please enter you last name: ")
lName = lName[0].upper() + lName[1:].lower()
city = input ("Please enter you city: ")
city = city[0].upper + city[1:]
hWage = float(input ("Please enter you hourly wage: "))
hWeek = float(input ("Please enter the number of hours you work each week: "))

weekSalary = hWage * hWeek
monthSalary = weekSalary *4
yearSalary = monthSalary *356
print("Hi, " + fName + " " + lName + "! How are you?")
print("I hope the weather is nice in " + city + ".")
print("Based on the information you provided, you earn $" +
      str(weekSalary) + " per week, approximately $" +
      str(monthSalary) + " per month, and $" +
      str(yearSalary) + " per year.")

