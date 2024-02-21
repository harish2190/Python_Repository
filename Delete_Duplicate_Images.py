#Delete Similar images from a directory or folder in Python

#The basic logic behind this python program is to create a hash value for each image not based on its name but based on its pixel value and count. 
#Based on this hash value we are going to store the images in a dictionary whose key will be the hash value generated and the value will hold the binary value of the image itself.
#Now based on this we store the images in a dictionary or if we find this as a duplicate we simply put this in the duplicate list having index and image binary form. Later on, 
#we delete this list of images based on their index value.

import hashlib
#from scipy.misc import imread, imresize, imshow
from matplotlib.pyplot import imread

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec  
import numpy as np
import os
def file_hash(filename):
    with open(filename,'rb') as f:
        return md5(f.read()).hexdigest()

folder=r'F:\Music\Songs\Random Songs'
os.getcwd()
os.chdir(folder)
os.getcwd()
files_list = os.listdir('.')
print(files_list)
print (len(files_list))
duplicates=[]
hash_keys=dict()
for index, filename in enumerate(os.listdir('.')):
    if os.path.isfile(filename):
        with open(filename, 'rb') as f:
            filehash = hashlib.md5(f.read()).hexdigest()
        if filehash not in hash_keys:
            hash_keys[filehash]=index
        else:
            duplicates.append((index,hash_keys[filehash]))
print(duplicates)
for file_indexes in duplicates[:30]:
    try:
        plt.subplot(121),plt.imshow(imread(files_list[file_indexes[1]]))
        plt.title(file_indexes[1]),plt.xticks([]),plt.yticks([])
        plt.subplot(122),plt.imshow(imread(files_list[file_indexes[0]]))
        plt.title(str(file_indexes[0])+ 'duplicate'),plt.xticks([]),plt.yticks([])
        #plt.show()
    except OSError as e:
        continue
for index in duplicates:
    print(files_list[index[0]])
    print('Deleted')
    os.remove(files_list[index[0]])
    
    
    
#Let’s understand the code:
#At first, we open the directory where we are going to work. This is done by changing the current directory to chdir(ie child directory)
#We then initialize a list and a dictionary
#Then we create a hash value for each image in that folder using hashlib.md5. this creates a 32-bit hash value.
#After this, with the help of this hash value, we store it in either a dictionary or a list.
#I am plotting the same images again for your better understanding in the try block. You can skip this part if you want.
#Finally, I am removing the duplicate images using os.remove

#The End