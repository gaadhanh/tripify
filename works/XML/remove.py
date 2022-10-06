import xml.etree.ElementTree as et
myroot=et.parse("modify.xml")
val=myroot.getroot()

print(val[0][0][3].text)
val[0].remove(val[0][0])
myroot.write("mod.xml")
