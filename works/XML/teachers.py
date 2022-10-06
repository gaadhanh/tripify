import xml.etree.ElementTree as et
myroot=et.parse("modify.xml")

val=myroot.getroot()
for i in val[1]:
    sal=int(i[3].text)
    i[3].text=str(sal+500)

myroot.write("modified.xml")