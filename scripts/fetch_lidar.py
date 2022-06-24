import pdal
import json
import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon
import json
from config import Config

class FetchLidar:
    def __init__(self) -> None:
        pass



    def make_pipeline(self, bounds: str, polygon_str: str, region: str, filename: str):
        
        with open('../assets/usgs_3dep_pipeline', 'r') as json_file:
            json_object = json.load(json_file)

        pipe = json_object
        pipe['pipeline'][0]['filename'] = Config.USGS_3DEP_PUBLIC_DATA_PATH / f"{region}/etp.json"
        pipe['pipeline'][0]['bounds'] = bounds
        pipe['pipeline'][1]['polygon'] = polygon_str
        pipe['pipeline'][6]['out_srs'] = f'EPSG:{self.output_epsg}'
        pipe['pipeline'][7]['filename'] = Config.ASSETS_PATH + f'{filename}.tif' 
        return pdal.Pipeline(json.dumps(pipe))




