import pandas as pd
import geopandas as gpd
from shapely import Point

from pccf_reader import read_pccf_data


def match_pccf_to_demo_data(post_code, pccf, da_data, da_spatial=None):
    pc_to_inspect = pccf[pccf.PCODE == post_code]
    if len(pc_to_inspect) == 0:
        pc_to_inspect = pccf[pccf.FSA == post_code[:3]]
        raise Exception("Zero PC Found")
    # if len(pc_to_inspect) >1:
    DAuid = list(set(pc_to_inspect.DAuid.to_list()))
    if len(DAuid) > 1:
        raise Exception("More than one PC Found")
    DAuid = DAuid[0]
    # DAuid = int(pc_to_inspect.DAuid)
    demo_data = da_data[da_data.ALT_GEO_CODE == DAuid]
    return ...


def read_demo_data_to_keep(demo_data_to_keep):
    with open(demo_data_to_keep) as f:
        lines = list(f.readlines())
    return [int(n.split('\t', 1)[0]) for n in lines]


if __name__ == "__main__":
    ProjLambert = "EPSG:3347"
    ProjWGS84 = "EPSG:4326"

    multi_pccf_file_da_weights = "C:/Users/seang/Dropbox/EO Data Project - Sean's Data Dump/PCCF8A/DATA/DA_Nat_weight_file_2021/DA_Nat_wgt_2021.txt"
    multi_pccf_file_da_weights = pd.read_fwf(
        multi_pccf_file_da_weights, header=None, widths=(6, 8, 5), names=["PCODE", "DAuid", "WEIGHT"])

    pccf_file_dups = "C:/Users/seang/Dropbox/EO Data Project - Sean's Data Dump/PCCF8A/DATA/PCCF2212.PCCF.DUPS.txt"
    pccf_file_uniq = "C:/Users/seang/Dropbox/EO Data Project - Sean's Data Dump/PCCF8A/DATA/PCCF2212.PCCF.UNIQ.txt"
    pccf_file = pd.concat([
        read_pccf_data(pccf_file_dups, ProjLambert, ProjWGS84),
        read_pccf_data(pccf_file_uniq, ProjLambert, ProjWGS84)
    ])

    da_data = "C:/Users/seang/Dropbox/EO Data Project - Sean's Data Dump/Census-Data-2021/98-401-X2021006_Ontario_eng_CSV/98-401-X2021006_English_CSV_data_Ontario.csv"
    demo_data_to_keep = "C:/Users/seang/Dropbox/EO Data Project/DemoDataShortlist.txt"
    demo_data_to_keep = read_demo_data_to_keep(demo_data_to_keep)
    da_data = pd.read_csv(da_data, encoding='ANSI')
    da_data = da_data[da_data.CHARACTERISTIC_ID.isin(demo_data_to_keep)]

    post_codes = [
        "M6P1G1",
        "N1P0B3",
        "K1H7S5",
        "K7K7J3",
        "N3Y2R6",
        "P1B9L8"
    ]
    for post_code in post_codes:
        print(post_code)
        match_pccf_to_demo_data(post_code, pccf_file, da_data)

    print("done!")
