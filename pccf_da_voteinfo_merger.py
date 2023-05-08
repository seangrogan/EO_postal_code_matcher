import pandas as pd
import geopandas as gpd
from shapely import Point

pccf_file_uniq = "C:/Users/seang/Dropbox/EO Data Project - Sean's Data Dump/PCCF8A/DATA/PCCF2212.PCCF.UNIQ.txt"
pccf_file_uniq = pd.read_csv(pccf_file_uniq, sep='\t', encoding="ANSI")
pccf_file_uniq = pccf_file_uniq[pccf_file_uniq.PR == 35]

pccf_file_uniq['geometry'] = pccf_file_uniq.apply(lambda x: Point(x["LONG"], x["LAT"]), axis=1)

da_spatial_data = "C:/Users/seang/Dropbox/EO Data Project - Sean's Data Dump/"

