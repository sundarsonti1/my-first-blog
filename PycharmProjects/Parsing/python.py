import os
from xml.etree import ElementTree

file_name = 'reed_college_courses.xml'
full_file = os.path.abspath(os.path.join('data', file_name))
dom = ElementTree.parse(full_file)

brand = dom.findall('Brand')