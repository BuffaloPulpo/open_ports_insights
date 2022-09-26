import glob
import os

from helpers import get_port_number_from_filepath, get_protocol_type_from_filepath

datasets_path = r"D:\all_rapid7_datasets_csv"
folder_path = datasets_path
dirs = os.listdir(folder_path)

all_files = glob.glob(folder_path+"/*")
# how many possible port number and associated network services?
set_of_port_numbers = set()
for file in all_files:
    print(file)
    port_number = get_port_number_from_filepath(file)
    print(port_number)
    set_of_port_numbers.add(port_number)
    protocol_type = get_protocol_type_from_filepath(file)
    print(protocol_type)
print(len(set_of_port_numbers))
print(set_of_port_numbers)
# extract port number, add it to set and see what we have

# for each port number, figure out the number of files, count of each and aggregate to avg count

# trend should be reserved for graph phase.
