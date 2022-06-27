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


    def plot_heatmap(df,column,title):
        fig, ax = plt.subplots(1, 1, figsize=(12, 10))
        fig.patch.set_alpha(0)
        plt.grid('on', zorder=0)
        df.plot(column=column, ax=ax, legend=True, cmap="terrain")
        plt.title(title)
        plt.xlabel('long')
        plt.ylabel('lat')
        plt.show()

    def plot_3d(self, s: float = 0.01) -> None:
        points = self.get_points()
        fig, ax = plt.subplots(1, 1, figsize=(12, 10))
        ax = plt.axes(projection='3d')
        ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=s)
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')
        plt.savefig(f'../assets/img/heatmap.png', dpi=120)
        plt.axis('off')
        plt.close()
        fig, ax = plt.subplots(1, 1, figsize=(12, 10))
        img = mpimg.imread('../assets/img/heatmap.png')
        imgplot = plt.imshow(img)
        plt.axis('off')
        plt.show()