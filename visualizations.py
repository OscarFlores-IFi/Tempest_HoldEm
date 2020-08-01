# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 14:54:41 2020

@author: Oscar
"""
import datashader as ds, pandas as pd
import datashader.transfer_functions as tf

def heatmap_datashader(lin):
    df = pd.DataFrame(lin,columns = ['x', 'y'])
    
    cvs = ds.Canvas(plot_width=800, plot_height=400)
    agg = cvs.points(df, 'x', 'y')
    img = tf.shade(agg, cmap=['lightblue', 'darkblue'], how='log')
    ds.transfer_functions.Image.border=0
    
    return(img)
    
    