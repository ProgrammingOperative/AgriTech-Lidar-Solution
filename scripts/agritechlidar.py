from shapely.geometry import Polygon
from fetch_lidar import FetchLidar
from vis import Vis



class AgriTechLidar:
    def __init__(self, epsg = 26915):
        self.input_epsg = 3857
        self.output_epsg = epsg
        self.fetch_data = FetchLidar(self.output_epsg)


    def fetch_lidar(self, polygon: Polygon, regions=[]):
        return self.fetch_data.get_lidar_data(polygon, regions)


    def render_vis(self, df: gpd.GeoDataFrame) -> Vis:
        return vis(df)
