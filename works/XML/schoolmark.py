import xml.etree.ElementTree as et
myroot=et.parse("school.xml")

val=myroot.getroot()
li=[]
for i in val[0]:
    li.append(int(i[5].text))
large=max(li)
for j in val[0]:
    if int(j[5].text)==large:
        print(j[1].text,":",j[5].text)
        




    


    
        