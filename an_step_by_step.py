#Importing math library
import math
#Asking the user for the value of A1
a1_str = input("What is A1: ")
a1 = int(a1_str)
#Asking the user for the value of Ω
omega_str = input("What is the Ω: ")
omega = int(omega_str)
#Asking the user for the value of N
n_str = input("What is the N: ")
n = int(n_str)
#Spliting the equation in different parts
#It also calculates the value of An
an1 = ((n) - 1)
an2 = ((an1) * (omega))
an3 = ((a1) + (an2))
#Printing the process of the evaluation of An in different parts
print("a",n," = ",a1," + (",n," - 1) * ",omega)
print("a",n," = ",a1," + (",an1,") * ",omega)
print("a",n," = ",a1," + (",an2,")")
print("a",n," = ",an3)
#Made by Avtovaz
#My GitHub: https://github.com/AvtoVAZ