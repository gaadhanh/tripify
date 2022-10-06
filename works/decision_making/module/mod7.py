word="python is a programming language"
li=list(word)
w="aeiou"
dic={}
for i in w:
    if i in li:
        dic[i]=li.count(i)
print(dic)