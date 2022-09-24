import glob
import os
import pandas as pd

path_3389_folder = r"C:\Users\Shuonan\Desktop\3389rdp"
folder_path = path_3389_folder
dirs = os.listdir(folder_path)

all_files = glob.glob(folder_path+"/*")
print(all_files)

intersected_ips = set()
print(len(intersected_ips))
for file in all_files:
    print(file)
    df = pd.read_csv(file)
    saddr_ips = set(df['saddr'].tolist())
    if len(intersected_ips) == 0:
        intersected_ips = intersected_ips.union(saddr_ips)
    else:
        intersected_ips = intersected_ips.intersection(saddr_ips)
    print(len(intersected_ips))
print(len(intersected_ips))


