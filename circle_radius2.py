# Write a Python program which accepts the radius of a circle from the user and compute the area. https://www.w3resource.com/python-exercises/python-basic-exercise-4.php
 
import os, sys, time        # only using these modules to make the program feel less clunky
import re                   # "Regular Expressions" is a module that makes setting exceptions for character input a lot simpler
import math
 
r = 0
p = math.pi
 
A = "A"
C = "C"
L = "L"   
 
#allowed_characters = ['A' , 'C', 'L']      # using re.match instead
 
 
# Variable input
 
while True:
    try:
        r = float(input("Radius of the circle: "))
        os.system("cls")
        print("The current value of r is: " + str(r))
        break
    except ValueError:
        print("Input must be digit")
        continue
 
 
# Defining the functions used for Proccessing + Answer
def circumference():
    answer = 2 * (p * r)
    print("The circumference of the circle is : " + str(answer))
 
def area():
    answer = p * r ** 2
    print("The Area of the circle is : " + str(answer))
 
 
 
# Choose to either calculate the Area or the Circumference or to leave
while True :
    AorC = input("Type (A) to calculate the area or (C) to calculate the circumferance or type (L) to leave : ").upper()
    if not re.match('^[ACL]*$',AorC):              # Using the "Regular Expression module" instead of setting up a for loop
        os.system("cls")
        print("Please enter A, C or L")
        continue
    elif A in AorC:
        area()
    elif C in AorC:
        circumference()
    elif L in AorC:
        os.system("cls")
        for count in range(3,0,-1):
            print("Leaving in " + str(count) + "seconds")
            time.sleep(1)
            os.system("cls")
        break
 
# Breaks the loop and exits the script