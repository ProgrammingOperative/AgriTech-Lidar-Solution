import pdal
import json
from bounds import Bounds
import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon
import json
from config import Config

class FetchLidar:
    def __init__(self) -> None:
        pass



    def make_pipeline(self, bounds: str, polygon_str: str, region: str, filename: str):
        
        with open('../assets/usgs_3dep_pipeline.json', 'r') as json_file:
            json_object = json.load(json_file)

        pipe = json_object
        pipe['pipeline'][0]['filename'] = Config.USGS_3DEP_PUBLIC_DATA_PATH / f"{region}/etp.json"
        pipe['pipeline'][0]['bounds'] = bounds
        pipe['pipeline'][1]['polygon'] = polygon_str
        pipe['pipeline'][6]['out_srs'] = f'EPSG:{self.output_epsg}'
        pipe['pipeline'][7]['filename'] = Config.DATA_PATH + f'{filename}.tif'
        pipe['pipeline'][8]['filename'] = Config.DATA_PATH + f'{filename}.tif' 
        return pdal.Pipeline(json.dumps(pipe))


    #   def get_dep(self, bounds: Bounds, polygon_str: str, region: list) -> gpd.GeoDataFrame:
    #   We only need the polygon, not necesarily the boundaries
   

    def fetch_data(self, bounds: Bounds, polygon_str: str, region: list) -> gpd.GeoDataFrame:
        """ Executes pdal pipeline and fetches point cloud data from a public repository.
            Using GDfHelper class creates Geopandas data frame containing geometry and elevation of the point cloud data.

        Args:
            bounds (Bounds): Geometry object describing the boundary of interest for fetching point cloud data
            polygon_str (str): Geometry object describing the boundary of the requested location.
            region (list): Point cloud data location for a specific boundary on the AWS cloud storage EPT resource. 

        Returns:
            gpd.GeoDataFrame: Geopandas data frame containing geometry and elevation
            """
        filename = region + "_" + bounds.get_bound_name()
        pl = self.make_pipeline(bounds.get_bound_str(),
                            polygon_str, region, filename)
        pl.execute()
        dep_data = self._gdf_helper.create_gdf(pl.arrays)
        return dep_data

    def get_lidar_data(self):
        bound, polygon_str = self._gdf_helper.get_bound_from_polygon(polygon)
        return self.fetch_data(bound, polygon_str)




