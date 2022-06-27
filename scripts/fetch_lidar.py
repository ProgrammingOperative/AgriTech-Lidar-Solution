import pdal
import json
from bounds import GeoBounds
import geopandas as gpd
from shapely.geometry import Polygon
import json
from gpd_helper import GpdHelper
from config import Config

class FetchLidar:
    def __init__(self, epsg: int = 26915) -> None:
        self.output_epsg = epsg
        self._input_epsg = 3857
        self._gdf_helper = GpdHelper(self._input_epsg, self.output_epsg)


    def make_pipeline(self, bounds: str, polygon_str: str, region: str, filename: str):
        
        with open('../assets/usgs_3dep_pipeline.json', 'r') as json_file:
            json_object = json.load(json_file)

        pipe = json_object
        pipe['pipeline'][0]['filename'] = Config.USGS_3DEP_PUBLIC_DATA_PATH / f"{region}/etp.json"
        pipe['pipeline'][0]['bounds'] = bounds
        pipe['pipeline'][1]['polygon'] = polygon_str
        pipe['pipeline'][5]['out_srs'] = f'EPSG:{self.output_epsg}'
        pipe['pipeline'][8]['filename'] = Config.DATA_PATH + f'{filename}.laz'
        pipe['pipeline'][9]['filename'] = Config.DATA_PATH + f'{filename}.tif' 
        return pdal.Pipeline(json.dumps(pipe))

    #   We only need the polygon, not necesarily the boundaries
   
    def fetch_data(self, bounds: GeoBounds, polygon_str: str, region: list) -> gpd.GeoDataFrame:
        filename = region + "_" + bounds.get_bound_name()
        pl = self.make_pipeline(bounds.get_bound_str(),
                            polygon_str, region, filename)
        pl.execute()
        gpd_data = self._gdf_helper.create_gdf(pl.arrays)
        return gpd_data


    def get_lidar_data(self, polygon, regions):
        bound, polygon_str = self._gdf_helper.get_bound_from_polygon(polygon)
        return self.fetch_data(bound, polygon_str, regions)




