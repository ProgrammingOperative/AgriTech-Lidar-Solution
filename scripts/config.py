from pathlib import Path


class Config:
  RANDOM_SEED = 42
  ROOT_PATH = Path("../")
  DATA_PATH = ROOT_PATH / "data/"
  ASSETS_PATH = ROOT_PATH / "assets/"
  USGS_3DEP_PUBLIC_DATA_PATH = "https://s3-us-west-2.amazonaws.com/usgs-lidar-public/"
