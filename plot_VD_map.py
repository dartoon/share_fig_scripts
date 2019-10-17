#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 22:59:09 2019

@author: Dartoon

Plot VD maps in the figure
"""
import numpy as np
import astropy.io.fits as pyfits
import matplotlib.pyplot as plt

import matplotlib.lines as mlines
import matplotlib as mat
mat.rcParams['font.family'] = 'STIXGeneral'


map_folder_true = 'fig_material/'
V_sigma =   pyfits.open(map_folder_true+'V_sigma.fits')[0].data.copy()    

V_mean =   pyfits.open(map_folder_true+'V_mean.fits')[0].data.copy()    
V_mean[V_mean==0] = np.nan

import copy, matplotlib
my_cmap1 = copy.copy(matplotlib.cm.get_cmap('coolwarm')) # copy the default cmap
my_cmap1.set_bad('snow') #linen

fig, ax = plt.subplots(figsize=(10,7))
plt.imshow(V_mean, cmap=my_cmap1, vmax = 200, vmin=-200)
clb = plt.colorbar()
clb.ax.tick_params(labelsize=25) 
clb.set_label(label='mean velocity (km/s)',fontsize=25,weight='bold')
plt.tick_params(labelsize=25)
plt.xticks([])
plt.yticks([])
#plt.savefig('fig_outputs/V_mean_map.pdf')
plt.show()

import copy, matplotlib
my_cmap2 = copy.copy(matplotlib.cm.get_cmap('gist_heat_r')) # copy the default cmap
my_cmap2.set_bad('seashell') #linen
V_sigma[V_sigma==-1] = np.nan
fig, ax = plt.subplots(figsize=(10,7))
plt.imshow(V_sigma, cmap=my_cmap2, vmax = 300, vmin=0)
clb = plt.colorbar()
clb.ax.tick_params(labelsize=25) 
clb.set_label(label='velocity dispersion (km/s)',fontsize=25,weight='bold')
plt.tick_params(labelsize=25)
plt.xticks([])
plt.yticks([])
#plt.savefig('fig_outputs/V_disp_map.pdf')
plt.show()
