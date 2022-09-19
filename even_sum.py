# even_sum.py
#
# 
def cSum (f,l):
    evens = []
    lower, higher = f if f <= l else l, l if f <= l else f
    i = lower+1
    while i < higher:
        if i%2 != 0:
            i+= 1
            continue    
        evens.append(i)
        i += 2
    print(sum(evens))
    
 

f, l = float(input("What is your first number: ")), float(input("What is your second number: "))   
cSum(f, l)