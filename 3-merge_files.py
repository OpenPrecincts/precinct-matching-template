'''
Merge together the clean precinct-level boundaries and precinct-level election results.

Expected input: CSV of election results, geospatial data with precinct boundaries
Expected output: Shapefile of precinct boundaries and columns for election results

'''

import geopandas as gpd
import pandas as pd
import numpy as np
import re

shp_path = "/Users/hopecj/projects/AR/Shapefiles/clean.shp"
elec_path = "/Users/hopecj/projects/gerryspam/AR/AR_G18.csv"

elec_df = pd.read_csv(elec_path)
shp_df = gpd.read_file(shp_path)

elec_df["elec_loc_prec"] = elec_df["county"] + "," + elec_df["precinct"].str.lower()
shp_df["shp_loc_prec"] = shp_df["county_nam"] + "," + shp_df["prec"].str.lower()
out = shp_df.merge(elec_df, left_on='shp_loc_prec', right_on='elec_loc_prec', how='outer')

out = out[['county_nam', 'state_fips', 'county_fip', 
           'PREC', 'precinct_x',  
           'G18DGOV', 'G18LGOV', 
           'G18RGOV', 'G18DATG',
           'G18RATG', 'G18LATG', 
           'G18DSecS', 'G18LSecS', 
           'G18RSecS', 'G18RTRES', 'G18LTRES', 
           'geometry']]

out = out.rename(columns={"precinct_x": "precinct_old", 
                       "prec": "precinct"})

out.to_file("/Users/hopecj/projects/AR/Shapefiles/ar18_final.shp")
