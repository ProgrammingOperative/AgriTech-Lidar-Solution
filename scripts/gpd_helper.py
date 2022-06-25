import numpy as np
import geopandas as gpd
from bounds import Bounds
from shapely.geometry import Point, Polygon



class GpdHelper:
    def __init__(self) -> None:
        self.input_epsg = input_epsg
        self.output_epsg = output_epsg
    

    def get_bound_from_polygon(self, polygon: Polygon) -> tuple:
        """ Computes bounds value for the given polygon

        Args:
            polygon (Polygon): Shapely geometry object describing the polygon.

        Returns:
            tuple: A tuple of Bounds object and a string of a given polygon in a form accepted by the pdal pipeline.
        """
        polygon_df = gpd.GeoDataFrame([polygon], columns=['geometry'])
        polygon_df.set_crs(epsg=self.output_epsg, inplace=True)
        polygon_df['geometry'] = polygon_df['geometry'].to_crs(epsg=self.input_epsg)
        xmin, ymin, xmax, ymax = polygon_df['geometry'][0].bounds
        bound = Bounds(xmin, xmax, ymin, ymax)
        x_cord, y_cord = polygon_df['geometry'][0].exterior.coords.xy
        polygon_str = self.get_polygon_str(x_cord, y_cord)

        return bound, polygon_str



