import glob
import os

datasets_path = r"D:\all_rapid7_datasets_csv"
folder_path = datasets_path
dirs = os.listdir(folder_path)

all_files = glob.glob(folder_path+"/*")
# how many possible port number and associated network services?
for file in all_files:
    print(file)
# for each port number, figure out the number of files, count of each and aggregate to avg count

# trend should be reserved for graph phase.
