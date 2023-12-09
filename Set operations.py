
def union(a,b):
    setunion=[]
    for i in range(0,len(a)):
        setunion.append(a[i])
    for j in range(0,len(b)):
        if(b[j] not in a):
            setunion.append(b[j])
    return setunion
# print(union(seta,setb))
def intersection(a,b):
    setinter=[]
    for i in range(0,len(a)):
        if(a[i] in b):
            setinter.append(a[i])
    return setinter
# print("Intersection")
# print(intersection(setc,setb))
def aminb(a,b):
    aminbset=[]
    for i in range(0,len(a)):
        if(a[i] not in b):
            aminbset.append(a[i])
    return aminbset
# print("a minus b set")
# print(aminb(setb,setc))
# print(aminb(setc,setb))
cric=[]
bad=[]
foot=[]
n=int(input("Enter the number of students :"))
for i in range(0,n):
    name=input("Enter the name :")
    a=int(input("1 for cricket"))
    b=int(input("1 for badminton"))
    c=int(input("1 for football"))
    if a==1:
        cric.append(name)
    if b==1:
        bad.append(name)
    if c==1:
        foot.append(name)
print("\ncricket :",cric,"\nBadminton :",bad,"\nFootball :",foot)
    
print("students who play both cricket and badminton",intersection(cric,bad))
print("Either cricket or badminton but not both ",union(aminb(cric,bad),aminb(bad,cric)))
print("Neither cricket nor badminton ",aminb(foot,union(cric,bad)))
print("Who play cricket and football but not badminton ",aminb(intersection(cric,foot),bad))
    
                
