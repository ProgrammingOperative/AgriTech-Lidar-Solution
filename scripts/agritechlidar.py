from shapely.geometry import Polygon
from fetch_lidar import FetchLidar
from visualization import Visualize
from gpd_helper import GpdHelper


class AgriTechLidar:
    def __init__(self, epsg = 26915):
        self.output_epsg = epsg
        self._input_epsg = 3857
        self._fetch_data = FetchLidar(self.output_epsg)


    def fetch_lidar(self, polygon: Polygon, regions=[]):
        return self._fetch_data.get_lidar_data(polygon, regions)


    def render_vis(self, df) -> Visualize:
        return Visualize(df)
