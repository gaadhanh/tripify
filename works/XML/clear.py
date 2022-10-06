import xml.etree.ElementTree as et
myroot=et.parse("modify.xml")
val=myroot.getroot()

val[1].clear()
myroot.write("mod.xml")