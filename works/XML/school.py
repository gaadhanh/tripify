import xml.etree.ElementTree as et
myroot=et.parse("school.xml")

val=myroot.getroot()
for i in val[0]:
        print(i[1].text)
    
        
    
