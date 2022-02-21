import geopandas as gpd
import pandas as pd
import fiona
from os import path, chdir, listdir, getcwd

dirname = getcwd()
kml_folder = path.join(dirname, 'dat')
shp_folder = path.join(dirname, 'out')
chdir(kml_folder)

gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'

dflist = []

for file in listdir():
    if file.endswith(".kml"):
        file_path = f"{kml_folder}/{file}"
        df = gpd.read_file(file_path, driver='KML')
        dflist.append(df)

print(f"Number of kml file red: {len(dflist)}")

omidf = gpd.geodataframe.GeoDataFrame()

for dfi in dflist:
    omidf = gpd.GeoDataFrame(pd.concat([omidf, dfi], ignore_index=True))

print("Dataframe Colums non nulls:")
print(omidf.count())

print("Generating Shapefile ...")
omidf.to_file(f"{shp_folder}/omi.shp")
