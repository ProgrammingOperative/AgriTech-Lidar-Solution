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

    def get_points(self):
        """ Generates a NumPy array from point clouds data.
        """
        x = self.df.geometry.x
        y = self.df.geometry.y
        z = self.df.elevation
        return np.vstack((x, y, z)).transpose()

    def plot_2d_heatmap(df,column,title):
        """
        plot a 2d heat map of the terrain
        args:
            df (geopndas df): a geopandas dataframe demonstrating the data
            column (str): input column to outline in string
            title (str): input title of the map in string
        return:
            2d heat map of terrain
        """
        fig, ax = plt.subplots(1, 1, figsize=(12, 10))
        fig.patch.set_alpha(0)
        plt.grid('on', zorder=0)
        df.plot(column=column, ax=ax, legend=True, cmap="terrain")
        plt.title(title)
        plt.xlabel('long')
        plt.ylabel('lat')
        plt.show()