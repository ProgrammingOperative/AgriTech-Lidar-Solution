import os
from glob import glob
import matplotlib.pyplot as plt
import rasterio as rio
from rasterio.plot import plotting_extent, show
import geopandas as gpd
import numpy as np
import geopandas as gpd
import matplotlib.image as mpimg
import rasterio
from rasterio.plot import show_hist



class Visualize():
    def __init__(self, df: gpd.GeoDataFrame):
        self.df = df

    
    def plot_raster(path_to_raster):
        """
        displays a raster from a .tif raster file
        args:
            path_to_raster (str): path to the raster file
        returns:
            rasterio image
        """
        src = rasterio.open(path_to_raster)
        fig, (axrgb, axhist) = plt.subplots(1, 2, figsize=(14,7))
        show((src), cmap='Greys_r', contour=True, ax=axrgb)
        show_hist(src, bins=50, histtype='stepfilled',
                lw=0.0, stacked=False, alpha=0.3, ax=axhist)
        plt.show()