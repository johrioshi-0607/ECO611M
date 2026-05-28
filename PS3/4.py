str1=str(input("Enter the string 1: "))
str2=str(input("Enter the string 2: "))
n=0
lst1=[]
lst2=[]


for i in range(0,len(str1)):
    for j in range(i+1,len(str1)+1):
        if str1[i:j] in str2:
            
            lst1.append(str1[i:j])
            lst2.append(len(str1[i:j]))
        else:
            break
a=max(lst2)
lst3=[]
while a in lst2:
    if lst1[lst2.index(a)] not in lst3:
        lst3.append(lst1[lst2.index(a)])
    lst1.pop(lst2.index(a))
    lst2.remove(a)

for i in lst3:
    print(i," ")




        
