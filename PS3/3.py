str1=str(input("enter the string 1:"))
str2=str(input("enter the string 2:"))
lst1=[]
lst2=[]

if len(str1)==len(str2):
    for ch in str1:
        lst1.append(ch)
    for ch in str2:
        lst2.append(ch)


    for ch1 in lst1:
        if ch1 in lst2:
            lst2.remove(ch1)
    

    if lst2==[]:
        print("PERMUTATION")
    else:
        print("NOT A PERMUTATION")
    
else:
    print("NOT A PERMUTATION")
    
