import random
def r():
    a=[]
    for i in range (1,11):
        a.append(random.randint(1,100))
    return a

def dob(a):
    b=[]
    for i in range(0,len(a)):
        b.append(a[i]*2)
    return b

def min(a):
    vmin=a[0]
    for i in range(0,len(a)):
        if a[i]< vmin :
            vmin=a[i]
    return vmin

def minmax(a):
    vmin=a[0]
    vmax=a[0]
    for i in range(0,len(a)):
        if a[i]< vmin :
            vmin=a[i]
        if a[i]> vmax :
            vmax=a[i]

    return vmin , vmax



a=r()
print(a)
print (sorted(a))
print(min(a))
print(minmax(a))
print(a)
print(dob(a))
