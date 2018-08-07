import os
import xml.etree.ElementTree as et

xml_file = '/home/sathish/Linux/XML/DB.xml'

tree = et.parse(xml_file)

root = tree.getroot()


new_user = et.SubElement(root, "user")
user_name = et.SubElement(new_user, "id")
user_password = et.SubElement(new_user, "password")

user_name.text = "568978"
user_password.text = "calc"

tree.write(xml_file)

print(root.tag)
for child in root:
    for element in child:
        print(element.tag, element.text)
