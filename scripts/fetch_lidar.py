import pdal
import json
import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon
import json


class FetchLidar:
    def __init__(self) -> None:
        pass



    def get_pipeline(self, bounds: str, polygon_str: str, region: str, filename: str):
        
        with open('../assets/usgs_3dep_pipeline', 'r') as json_file:
            json_object = json.load(json_file)

        pipe = json_object
        pipe['pipeline'][0]['filename'] = path
        pipe['pipeline'][0]['bounds'] = bounds
        pipe['pipeline'][1]['polygon'] = polygon_str
        pipe['pipeline'][6]['out_srs'] = f'EPSG:{self.output_epsg}'
        pipe['pipeline'][7]['filename'] = path
        pipe['pipeline'][8]['filename'] = path
        return pdal.Pipeline(json.dumps(pipe))




