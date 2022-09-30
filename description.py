import collections
import glob
import os
import pandas as pd
from helpers import get_port_number_from_filepath, get_protocol_type_from_filepath

pd.set_option('display.max_rows', 1000)

datasets_path = r"D:\all_rapid7datasets"
folder_path = datasets_path
dirs = os.listdir(folder_path)

all_files = glob.glob(folder_path+"/*")
# how many possible port number and associated network services?
list_of_port_numbers = list()
# for file in all_files:
#     port_number = get_port_number_from_filepath(file)
#     if 'udp' not in file:
#         list_of_port_numbers.append(port_number)
# print(list_of_port_numbers)
# data = pd.Series(list_of_port_numbers)
# print(data.value_counts())
# extract port number, add it to set and see what we have

# for each port number, figure out the number of files, count of each and aggregate to avg count

# trend should be reserved for graph phase.
