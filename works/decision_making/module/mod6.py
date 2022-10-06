word="Python is a programming langage"
dic={'a':0,'e':0,'i':0,'o':0,'u':0}
for i in word:
    if i=='a':
        dic['a']+=1
    elif i=='e':
        dic['e']+=1
    elif i=='i':
        dic['i']+=1
    elif i=='o':
        dic['o']+=1
    elif i=='u':
        dic['u']+=1
    
 
print(dic)