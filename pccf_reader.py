import pandas as pd
from shapely import Point
import geopandas as gpd

# pccf_file_uniq = "C:/Users/seang/Dropbox/EO Data Project - Sean's Data Dump/PCCF8A/DATA/PCCF2212.PCCF.UNIQ.txt"
# pccf_file_dups = "C:/Users/seang/Dropbox/EO Data Project - Sean's Data Dump/PCCF8A/DATA/PCCF2212.PCCF.DUPS.txt"
#
# pccf_file_uniq = pd.read_csv(pccf_file_uniq, sep='\t', encoding="ANSI")
# pccf_file_dups = pd.read_csv(pccf_file_dups, sep='\t', encoding="ANSI")
#
# pccf_file_uniq = pccf_file_uniq[pccf_file_uniq.PR == 35]
# pccf_file_dups = pccf_file_dups[pccf_file_dups.PR == 35]


def remove_postal_code_spaces(df, postcode_col, new_col=False):
    if new_col is False:
        df[postcode_col] = df[postcode_col].str.replace(' ', '')
        return df
    else:
        if isinstance(new_col, bool):
            new_col = "PCODE_NOSPACE"
        df[new_col] = df[postcode_col].str.replace(' ', '')
        return df




def read_pccf_data(pccf_filename, TargetProjection, ProjWGS84="EPSG:4326"):
    # pccf_filename = "C:/Users/seang/Dropbox/EO Data Project - Sean's Data Dump/PCCF8A/DATA/PCCF2212.PCCF.DUPS.txt"
    pccf_file = pd.read_csv(pccf_filename, sep='\t', encoding="ANSI")
    pccf_file = pccf_file[pccf_file.PR == 35]
    pccf_file['geometry'] = pccf_file.apply(lambda x: Point(x["LONG"], x["LAT"]), axis=1)
    pccf_file = gpd.GeoDataFrame(pccf_file).set_crs(ProjWGS84).to_crs(TargetProjection)
    return pccf_file
