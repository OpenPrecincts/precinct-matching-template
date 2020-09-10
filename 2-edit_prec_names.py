'''
Clean geospatial precinct names.

Expected input: Geospatial file with precincts as rows
Expected output: Geospatial file with precincts as rows, and precinct names that match the ones in the election results

'''

import geopandas as gpd
import pandas as pd

shp_path = ''
elec_path = ''

elec_df = pd.read_csv(elec_path)
shp_df = gpd.read_file(shp_path)
shp_df = shp_df[["state_fips", "county_fip",
                 "county_nam", "precinct", "geometry"]]

"""
general helper functions for all counties
"""

def chop_five(dat):
    dat["prec"] = dat["prec"].str.slice(start=5)
    
# ignore special election rows 
# mail-in, provisional, emergency, hand(?), overseas, removed resident, congressional district tallies
def ignore_special(df):
    patternDel = """mail|vbm|prov|emergency|oversea|hand|total|
                not defined|removed|remove|congressional|th cong|
                unassigned|contest|rejected|presidential"""
    filter = df[~df["precinct"].str.contains(patternDel, na=False)]
    return filter

"""
county-specific cleaning counties
"""

def ashley(dat):
    chop_five(dat)
    dat["prec"] = dat["prec"].replace({
        "Crossett Ward 1": "CW1",
        "Crossett Ward 2": "CW2",
        "Crossett Ward 3": "CW3",
        "Cross Roads": "CROSSROADS",
        "Fountain Hill City": "FH CITY",
        "Fountain Hill Rural": "FH RURAL",
        "Hamburg Ward 1": "HW1",
        "Hamburg Ward 2": "HW2",
        "Hamburg Ward 3": "HW3",
        "Mt. Zion": "MT ZION",
        "North Crossett East": "NCE",
        "North Crossett West": "NCW",
        "Snyder / Trafalgar": "SNY/TRA",
        "VO - Tech": "VOTECH",
        "West Crossett Rural": "WCR",
    })

def baxter(dat):
    dat["prec"] = dat["prec"] + "b"

def boone(dat):
    dat["prec"] = dat["prec"].replace(
        {
            "Diamond City (12)": "District 12",
        })

def carroll(dat):
    dat["prec"] = dat["prec"].replace(
        {
            "Berryville Ward 1": "BV Ward 1",
            "Berryville Ward 2": "BV Ward 2",
            "Eureka Springs Ward 1": "ES Ward 1",
            "Eureka Springs Ward 2": "ES Ward 2",
            "Eureka Springs Ward 3": "ES Ward 3",
            "Green Forest Ward 1": "GF Ward 1",
            "Green Forest Ward 2": "GF Ward 2",
            "North East Hickory": "NE Hickory",
            "Northwest Hickory": "NW Hickory",
            "Long Creek": "Lng Crk",
            "SW & SE Hickory": "SW/SE HICKORY",
        })

def chicot(dat):
    chop_five(dat)
    dat["prec"] = dat["prec"].replace(
        {" Carlton": "Carlton 1 & 2",
         " Carlton 2": "Carlton 1 & 2",
         })

def clay(dat):
    chop_five(dat)
    dat["prec"] = dat["prec"].replace(
        {
            "Bennett & Lemmons": "Bennett and Lemmons",
            "E Oak Bluff & Blue Cane": "East Oak Bluff & Blue Cane",
            "Liddell & chalk Bluff": "Liddell & Chalk Bluff",
            "Cleveland & N Kilgore": "N Kilgore & Cleveland",
            "North St Francis": "North St. Francis",
            "Gleghorn & S Kilgore": "S Kilgore & Gleghorn",
            "South St Francis": "South St. Francis",
        })
    
def cleveland(dat):
    chop_five(dat)
    dat["prec"] = dat["prec"].replace(
        {" Kingsland Out": "Kingsland outside", })

def columbia(dat):
    dat["prec"] = dat["prec"].replace(
        {"Taylor City": "Taylor", "Waldo City": "Waldo"})

def conway(dat):
    dat["prec"] = dat["prec"].str.slice(start=6)
    dat["prec"] = dat["prec"].replace(
        {"St Vincent": "St. Vincent", 
         "Lick Mountain": "Lick Mtn.",
         "Morrilton Ward 1": "Ward 1",
         "Morrilton Ward 2": "Ward 2",
         "Morrilton Ward 3": "Ward 3",
         "Morrilton Ward 4": "Ward 4",
         "nifee City": "menifee city",
         })

def crawford(dat):
    dat["prec"] = dat["prec"].replace(
        {
            "Alma 01": "Alma 1",
            "Alma 02": "Alma 2",
            "Alma 03": "Alma 3",
            "Alma 04": "Alma 4",
            "Cove City": "Cove City CSD",
            "Lee Creek": "Lee Creek CSD",
            "Mulberry 01": "Mulberry 1",
            "Mulberry 02": "Mulberry 2",
            "Mulberry 03": "Mulberry 3"})

def cross(dat):
    dat["prec"] = dat["prec"].replace(
        {
            "Bay Village / Birdeye": "Bay Village, Birdeye",
            "Cherry Valley": "Cherry Valley City",
            "Tyronza / Twist": "Tyronza, Twist",
            "Wynne Ward 1": "WYNNE WARD 1",
            "Wynne Ward 2": "WYNNE WARD 2",
            "Wynne Ward 3": "WYNNE WARD 3",
            "Wynne Ward 4": "WYNNE WARD 4",
            "Wynne Ward 5": "WYNNE WARD 5"})

def dallas(dat):
    chop_five(dat)
    dat["prec"] = dat["prec"].replace(
        {" District 5 -": "district 5", 
    })

def desha(dat):
    chop_five(dat)
    dat["prec"] = dat["prec"].replace(
        {
            "Bowie W1": "Bowie 1",
            "Bowie W2": "Bowie 2",
            "Bowie W3": "Bowie 3",
            "Mitcheville": "Mitchellville",
            "Rand W1": "Randolph 1",
            "Rand W2": "Randolph 2",
            "Rand W3": "Randolph 3",
            "Rand W4": "Randolph 4",
            "Rand Rural": "Randolph Rural",
            "Silver Lake": "Silverlake",
        })

def drew(dat):
    chop_five(dat)
    dat["prec"] = dat["prec"].replace(
        {
            "Mar N Box 1": "MN BOX 1 - RH Cumb. Presb",
            "Mar N Box 2": "MN Box 2 - RH Baptist Chu",
            "Marion South": "Marion South - Shady Grov",
        })

def fulton(dat):
    dat["prec"] = dat["prec"].replace(
        {"MS - Afton": "MAMMOTH SPRING/AFTON",
         "Fulton - Mt. Calm": "FULTON/MT CALM"
         })
    dat["prec"] = dat["prec"].str.replace(" - ", "/")

def garland(dat): 
    dat["prec"] = dat["prec"].str.lstrip("0")

def hempstead(dat):
    dat["prec"] = dat["prec"].str.slice(start=3)
    dat["prec"] = dat["prec"].replace(
        {"Cross Roads": "Crossroads",
         })

def hotspring(dat):
    dat["prec"] = dat["prec"].replace(
        {"Friendship City": "Friendship",
        "Malvern W-1": "ward 1",
        "Malvern W-2": "ward 2",
        "Malvern W-3": "ward 3",
        "Malvern W-4": "ward 4",
        })

def howard(dat):
    chop_five(dat)
    dat["prec"] = dat["prec"].replace(
        {
        "ineral Spring 3": "Mineral spring 3",
        })

def lafayette(dat):
    dat["prec"] = dat["prec"].str.slice(start=6)
    dat["prec"] = dat["prec"].replace(
        {
            "Stamps Ward 1, Prec 1": "Stamps Ward 1, Pct 1",
            "Stamps Ward 1, Prec 2": "Stamps Ward 1, Pct 2",
            "Bradley City": "Bradley",
            "Buckner City": "Buckner",
            "Lewisville Out": "Lewisville Ward 1 (Out)",
            "Stamps W1 P2 Out": "Stamps Ward 1, Pct 2 (Out)",
            "Stamps W2 Out": "Stamps Ward 2 (Out)",
            "Buckner Out": "Buckner (Out)",
            "Bradley Out": "Bradley (Out)",
        })

def marion(dat):
    dat["prec"] = "P00" + dat["prec"].str.slice(start=9)

def pope(dat):
    chop_five(dat)
    dat["prec"] = dat["prec"].str.replace("-", "")

def pulaski(dat):
    dat["prec"] = dat["prec"].str.slice(start=9)
    dat["prec"] = dat["prec"].str.lstrip("0")

def saline(dat):
    dat["prec"] = "Precinct " + dat["prec"]

def scott(dat):
    chop_five(dat)
    dat["prec"] = dat["prec"].replace(
        {
            "Lewis 1": "Lewis Ward 1",
            "Lewis 2": "Lewis Ward 2",
            "Lewis 3": "Lewis Ward 3",
            "Mt. Pleasant": "Mount Pleasant",
        })

def sebastian(dat):
    dat["prec"] = dat["prec"].str.slice(start=9)

"""
overall call function
"""
countyToCountyCleaner = {
    "Ashley": ashley,
    "Baxter": baxter,
    "Boone": boone,
    "Carroll": carroll,
    "Chicot": chicot,
    "Clay": clay,
    "Cleburne": chop_five,
    "Cleveland": cleveland,
    "Columbia": columbia,
    "Conway": conway,
    "Crawford": crawford,
    "Cross": cross,
    "Dallas": dallas,
    "Desha": desha,
    "Drew": drew,
    "Fulton": fulton,
    "Garland": garland,
    "Grant": chop_five,
    "Hempstead": hempstead,
    "Hot Spring": hotspring,
    "Howard": howard,
    "Lafayette": lafayette,
    "Pike": chop_five,
    "Pulaski": pulaski,
    "Saline": saline,
    "Sebastian": sebastian,
    "Scott": scott,
    "Yell": chop_five,
}

# to test for select counties
# raw_df = shp_df.loc[
#    (shp_df['county_nam'] == "Desha") |
#    (shp_df['county_nam'] == "Benton") |
#    (shp_df['county_nam'] == "Woodruff")]

# remove special election precinct rows 
print(shp_df.shape)
shp_df = ignore_special(shp_df)
print(shp_df.shape) # got rid of X rows

# must sort alphabetically in order for second-order function to work
clean_df = shp_df.sort_values(by=['county_nam'])

counties = pd.Series(clean_df['county_nam']).unique()
clean_df["prec"] = clean_df["precinct"].copy()
clean_df.set_index(['county_nam', 'precinct'], inplace=True)
print("duplicated indices", clean_df[clean_df.index.duplicated()])

for county in counties:
    county_dat = clean_df.loc[county]
    changed = countyToCountyCleaner.get(county, lambda x: x)(county_dat)
    clean_df.update(county_dat)

clean_df['prec'] = clean_df['prec'].str.lower()
clean_df.reset_index(inplace=True)

clean_df.to_file("/Users/hopecj/projects/AR/Shapefiles/1_edited_precnames/clean.shp")