import xml.etree.ElementTree as ET
import os
import cv2
import numpy as np
import random

def cutout(img, gt_boxes, amount=0.05):
    '''
    ### Cutout ###
    img: image
    gt_boxes: format [[obj x1 y1 x2 y2],...]
    amount: num of masks / num of objects
    '''
    out = img.copy()
    #ran_select = random.sample(gt_boxes, round(amount*len(gt_boxes)))

    for box in gt_boxes:
        #print('box',box)
        #print('ran_select',ran_select)
        x1 = int(box[1])
        y1 = int(box[2])
        x2 = int(box[3])
        y2 = int(box[4])
        mask_w = int((x2 - x1)*random.uniform(0.1, 0.6))
        mask_h = int((y2 - y1)*random.uniform(0.1, 0.7))
        mask_x1 = random.randint(x1, x2 - mask_w)
        mask_y1 = random.randint(y1, y2 - mask_h)
        mask_x2 = mask_x1 + mask_w
        mask_y2 = mask_y1 + mask_h
        print('mask_x1',mask_x1)
        print('mask_y1',mask_y1)
        print('mask_x2',mask_x2)
        print('mask_y2',mask_y2)
        cv2.rectangle(out, (mask_x1, mask_y1), (mask_x2, mask_y2), (0, 0, 0), thickness=-1)
    return out

path = "all_xml"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")
print("length: ", len(dir_list))

# prints all files
print(dir_list)

for elem in dir_list:
    x_name = elem.split(".", 1)
    #print(x[0])

    xml_name=x_name[0]+".xml"
    jpg_name=x_name[0]+".jpg"

    xmin=[]
    ymin=[]
    xmax=[]
    ymax=[]
    sum=[]
    root_node = ET.parse('all_xml/'+xml_name).getroot()

    for tag in root_node.findall('object/bndbox/xmin'):
        xmin.append(tag.text)
        print(tag.text)

    for tag in root_node.findall('object/bndbox/ymin'):
        ymin.append(tag.text)
        print(tag.text)

    for tag in root_node.findall('object/bndbox/xmax'):
        xmax.append(tag.text)
        print(tag.text)

    for tag in root_node.findall('object/bndbox/ymax'):
        ymax.append(tag.text)
        print(tag.text)


    asd=len(xmin)
    for i in range(asd):
        a=[i,xmin[i],ymin[i],xmax[i],ymax[i]]
        sum.append(a)


    #for i in range(asd):
     #   print(sum[i])

    path2 = "LUCAS2009_AS+/"+jpg_name

    # Reading an image in default mode
    image = cv2.imread(path2)
    #image =cv2.resize(image,(416,416))
    #cv2.imshow("image", image)

    asdasd =cutout(image,sum,0.5)

    #ig=cv2.resize(asdasd,(416,416))
    #cv2.imshow("window_name", asdasd)


    catout_name=x_name[0]+"_CutOut.jpg"
    cv2.imwrite('cutout/'+catout_name, asdasd)

    cv2.waitKey(0)

    # closing all open windows
    cv2.destroyAllWindows()








