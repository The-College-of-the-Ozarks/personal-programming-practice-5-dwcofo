# sqrt.py
#
# 

def crackSqrt(num, e):
    
    x = num/2
    while abs(x**2 - num) > e:
        x = (x+num/x)/2
    return x
    
    
n, epsilon = float(input("What number do you want to find the sqrt of: ")), float(input("How close do you want x to be: "))

x = crackSqrt(n, epsilon)

print("Your number is", n,"and you wanted to be",epsilon,"close.\nMy guess is x which is",x,". When you square it", x**2)