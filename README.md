# AgriTechLidar

## Scenario 
You work at an AgriTech, which has a mix of domain experts, data scientists, data engineers. As part of the data engineering team, you are tasked to produce an easy to use, reliable and well designed python module that domain experts and data scientists can use to fetch, visualise, and transform publicly available satellite and LIDAR data. In particular, your code should interface with USGS 3DEP and fetch data using their API. 

You may search for open source python packages and adapt them to your needs, or you may choose to write everything from scratch. In the former case, please be clear about attributing where the work and code came from - this is essential.  


## Overview
AgriTechLidar is a package that can fetch point cloud data from the public lidar point cloud data hosted in an amazon s3 bucket, query the data model to select with  a specified boundary (GPS coordinate polygon) to return 
a raster of the height of the terrain within the boundary, visualize the terraine and transform the data to determine other features like Topographic wetness index (TWI).


## Requirements
- PDAL
- GEOPANDAS
- LASPY



## Data
The resource in the s3 bucket is in entwine format, EntwinePoint Tile (EPT) is a simple and flexible octree-based storage format for point cloud data. The organization of an EPT dataset contains JSON metadata portions as well as binary point data. The JSON file is core metadata required to interpret the contents of an EPT dataset.



# Install

```
pip install AgriTechLidar

```

## Usage


