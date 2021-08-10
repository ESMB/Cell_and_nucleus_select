#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 10:24:11 2021

@author: Mathew
"""


from skimage.io import imread
import os
import pandas as pd
from picasso import render
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

import napari 
# Change paths to the images:
    
path=r"/Volumes/VERBATIM HD/Data_For_Mathew/1w_old_neurons_Apt_and_Phalloidin_DAPI/"
dapi="1w_C1_dapi.tif"




def load_image(toload):
    
    image=imread(toload)
    
    return image

def view_image(input_image,nuclei,cells):
    with napari.gui_qt():
        
            viewer = napari.Viewer()
            
            viewer.add_image(input_image)
            viewer.add_labels(nuclei,name='Nuclei')
            viewer.add_labels(cells, name='Cells')
    return nuclei,cells       
    
dapi_image=load_image(path+dapi)

nuclei=np.zeros(np.shape(dapi_image),dtype=int)
cells=np.zeros(np.shape(dapi_image),dtype=int)

nuclei_label,cells_label=view_image(dapi_image,nuclei,cells)

plt.imshow(nuclei_label)
plt.show()
plt.imshow(cells_label)
plt.show()


imsr = Image.fromarray((nuclei_label).astype(np.uint8))
imsr.save(path+'nuclei.tif')

imsr = Image.fromarray((cells_label).astype(np.uint8))
imsr.save(path+'cell.tif')

