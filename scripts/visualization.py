import os
from glob import glob
import matplotlib.pyplot as plt
import rasterio as rio
from rasterio.plot import plotting_extent
import geopandas as gpd
import numpy as np
import geopandas as gpd
import matplotlib.image as mpimg



class Visualize():
    def __init__(self, df: gpd.GeoDataFrame):
        self.df = df