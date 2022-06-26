from shapely.geometry import Polygon
from fetch_lidar import FetchLidar
from vis import Vis





class AgriTechLidar:
    def __init__(self, epsg = 26915):
        self.input_epsg = epsg
        self.output_epsg = 3857
        self.fetch_data = FetchLidar(self.output_epsg)


    def fetch_lidar(self, polygon: Polygon):
        return self.fetch_data(polygon)


    def render_vis(self, df: gpd.GeoDataFrame) -> Vis:
        return vis(df)
