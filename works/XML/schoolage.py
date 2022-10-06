from operator import gt
import xml.etree.ElementTree as et
myroot=et.parse("school.xml")

val=myroot.getroot()
for i in val[0]:
    if int(i[4].text) > 25:
        print(i[1].text)
    
        