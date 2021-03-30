# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 21:40:13 2021

@author: Admin
"""

"""  CALCULATOR """

def addition():
    print("Addition")
    n = float(input("Enter the number"))
    tno = 0
    res =0
    while n!=0:
        res+=n
        tno+=1
        n=float(input("Enter the number (enter 0 to stop):"))
    return [res,tno]

def subtraction():
    print("Subtraction")
    n=[]
    tno=1
    i=1
    while i>0:
        i=float(input("Enter the number (enter 0 to stop):") )
        n.append(i)
    n.remove(n[len(n)-1])
    print(n)
    res=n[0]
    for a in range(1,len(n)):
        res-=n[a]
        tno+=1
    return [res,tno]

def multiplication():
    print("Multiplication")
    n= float(input("Enter the number"))
    tno=0
    res=1
    while n!=0:
        res*=n
        tno+=1
        n=float(input("Enter the number(enter 0 to stop):"))
    return [res,tno]

def division():
    print("Division")
    n=[]
    tno=1
    #n=input("Enter the number")
    i=1
    while i>0:
        i=float(input("Enter the number (enter 0 to stop):") )
        n.append(i)
    n.remove(n[len(n)-1])
    print(n)
    res=n[0]
    for a in range(1,len(n)):
        res/=n[a]
        tno+=1
    return [res,tno]


while True:
    print("Calculator")
    print("Enter 'a' for Addition")
    print("Enter 's' for Subtraction")
    print("Enter 'm' for Multiplication")
    print("Enter 'd' for Division")
    print("Enter 'q' for Quit")
    c=input(" ")
    if c!='q':
        if c=='a':
            list = addition()
            print("Sum = ",list[0], "Total Inputs = ", list[1])
        elif c=='s':
            list = subtraction()
            print("Subtraction = ", list[0], "Total Inputs = ", list[1])
        elif c=='m':
            list = multiplication()
            print("Multiplication =", list[0], "Total Inputs = ", list[1])
        elif c=='d':
            list = division()
            print("Division =", list[0], "Total Inputs = ", list[1])
        else:
            print("Invalid Choice")
    else:
        break
    
        



