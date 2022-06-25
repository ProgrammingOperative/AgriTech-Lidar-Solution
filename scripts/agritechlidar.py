from shapely.geometry import Polygon
from fetch_lidar import FetchLidar
from vis import Vis





class AgriTechLidar:
    def __init__(self) -> None:
        pass

    def fetch_lidar(self, polygon: Polygon):
        return self.fetch_lidar(polygon)


    def render_vis(self, df: gpd.GeoDataFrame) -> Vis:
        return vis(df)
