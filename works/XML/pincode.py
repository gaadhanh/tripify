import xml.etree.ElementTree as et
myroot=et.parse("modify.xml")
val=myroot.getroot()

et.SubElement(val[0][0],"pincode")
for i in val.iter("picode"):
    i.text=str(686501)

myroot.write("mod.xml")
