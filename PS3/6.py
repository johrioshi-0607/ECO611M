str=str(input("enter the string "))
sets={'a','e','i','o','u','A','E','I','O','U'}
set1=set()

for i in range(0,len(str)):
  if str[i] in sets:
    for j in range(i,len(str)+1):
        set1=set()
        set1.update(str[i:j].split())
        if set1.issubset(sets):
            print(str[i:j],str.index(str[i:j]))
  else:
      continue
