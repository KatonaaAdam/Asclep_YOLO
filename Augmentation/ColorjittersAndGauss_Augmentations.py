import random

import cv2
import numpy
import os

import numpy as np




# Get the list of all files and directories

path = "colorjitter_b/colorjitter_b_xml"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")
print("length: ", len(dir_list))

# prints all files
print(dir_list)


# Renaming the file

for elem in dir_list:
    print(elem)
    x = elem.split(".", 1)
    print(x[0] + "_colorjitter_typeB.xml")
    old_name="colorjitter_b/colorjitter_b_xml/"+elem
    new_name="colorjitter_b/colorjitter_b_xml/"+x[0]+"_colorjitter_typeB.xml"
    os.rename(old_name, new_name)


#Gauss zajterhelés
"""
for elem in dir_list:
    print(elem)
    x = elem.split(".", 1)
    #print(x[0])
    src = cv2.imread('LUCAS2009_AS+/'+elem, cv2.IMREAD_UNCHANGED)
    dst = cv2.GaussianBlur(src, (5, 5), cv2.BORDER_DEFAULT)
    name=x[0]+"_blur.jpg"
    cv2.imwrite('Gblur/'+name, dst)
"""

#ellenőrzés
"""
path2 = "Gblur"
dir_list2 = os.listdir(path2)
print("Files and directories in '", path2, "' :")
print("length: ", len(dir_list2))

# prints all files
print(dir_list2)

cv2.destroyAllWindows()
"""


def colorjitter(img, cj_type="c"):
    '''
    ### Different Color Jitter ###
    img: image
    cj_type: {b: brightness, s: saturation, c: constast}
    '''
    if cj_type == "b":
        # value = random.randint(-50, 50)
        value = np.random.choice(np.array([-50, -40, -30, 30, 40, 50]))
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        if value >= 0:
            lim = 255 - value
            v[v > lim] = 255
            v[v <= lim] += value
        else:
            lim = np.absolute(value)
            v[v < lim] = 0
            v[v >= lim] -= np.absolute(value)

        final_hsv = cv2.merge((h, s, v))
        img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        return img

    elif cj_type == "s":
        # value = random.randint(-50, 50)
        value = np.random.choice(np.array([-50, -40, -30, 30, 40, 50]))
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        if value >= 0:
            lim = 255 - value
            s[s > lim] = 255
            s[s <= lim] += value
        else:
            lim = np.absolute(value)
            s[s < lim] = 0
            s[s >= lim] -= np.absolute(value)

        final_hsv = cv2.merge((h, s, v))
        img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        return img

    elif cj_type == "c":
        brightness = 10
        contrast = random.randint(40, 100)
        dummy = np.int16(img)
        dummy = dummy * (contrast / 127 + 1) - contrast + brightness
        dummy = np.clip(dummy, 0, 255)
        img = np.uint8(dummy)
        return img


def filters(img, f_type="blur"):
    '''
    ### Filtering ###
    img: image
    f_type: {blur: blur, gaussian: gaussian, median: median}
    '''
    if f_type == "blur":
        image = img.copy()
        fsize = 9
        return cv2.blur(image, (fsize, fsize))

    elif f_type == "gaussian":
        image = img.copy()
        fsize = 9
        return cv2.GaussianBlur(image, (fsize, fsize), 0)

    elif f_type == "median":
        image = img.copy()
        fsize = 9
        return cv2.medianBlur(image, fsize)

path = "LUCAS2009_AS+/2009_49022644E_V.jpg"

# Reading an image in default mode
image = cv2.imread(path)
image =cv2.resize(image,(416,416))
cv2.imshow("image", image)

img =filters(image,"median")

cv2.imshow("window_name", img)

cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()



"""
for elem in dir_list:
    print(elem)
    x = elem.split(".", 1)
    #print(x[0])
    src = cv2.imread('LUCAS2009_AS+/'+elem, cv2.IMREAD_UNCHANGED)
    dst = colorjitter(src,"s")
    name=x[0]+"_colorjitter_typeS.jpg"
    cv2.imwrite('colorjitter_s/'+name, dst)
"""

"""
path = "LUCAS2009_AS+/2009_49022644E_V.jpg"

# Reading an image in default mode
image = cv2.imread(path)
cv2.imshow("window_name", image)

cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()"""