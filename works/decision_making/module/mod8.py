word="python is a programming language"
li=set(word)
dic={}
for i in word:
    if i in li:
        dic[i]=word.count(i)
print(dic)