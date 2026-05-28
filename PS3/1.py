str=str(input("enter the string: "))
lower=0
upper=0
digit=0
spe_char=0

for ch in str:
    if ch.islower():
        lower+=1
    elif ch.isupper():
        upper+=1
    elif ch.isdigit():
        digit+=1
    else:
        spe_char+=1
print("lower=",lower)
print("upper=",upper)
print("digits=",digit)
print("special characters=",spe_char)
