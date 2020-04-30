import xml.etree.ElementTree as ET
from os import getcwd

sets=['train', 'val','test']

classes = ["echinus","holothurian","scallop","starfish","waterweeds"]


def convert_annotation(image_id, list_file):
    in_file = open('/home/drive/data/underwater/train/box/%s.xml'%(image_id))
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        #difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes:# or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = getcwd()
print(wd,"\n")
image_ids = open('/home/drive/data/underwater/data/test.list').read().strip().split()
list_file = open('/home/drive/data/underwater/data/test_image_annotation.txt', 'w')
for image_id in image_ids:
    print(image_id)
    image_id = image_id.rsplit('/',1)[1].split('.')[0]
    list_file.write('/home/drive/data/underwater/data/test/%s.jpg'%(image_id))
    convert_annotation(image_id, list_file)
    list_file.write('\n')
list_file.close()

