def Intersection(n1,n2):
    a1=0
    a2=0
    for i in n1:
        if i in n2:
            a1+=1
    for i in n2:
        if i in n2:
            a2+=1
    return[a1,a2]
n1=list(map(int,input("enter n1:").split()))
n2=list(map(int,input("Enter n2:").split()))
print(Intersection(n1,n2))