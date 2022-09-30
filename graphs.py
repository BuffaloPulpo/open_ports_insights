import glob
import os
import pandas as pd
from helpers import get_port_number_from_filepath, get_protocol_type_from_filepath
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 1000)

datasets_path = r"C:\Users\Shuonan\Desktop\qotd_17"




def plot(folder_path):
    dirs = os.listdir(folder_path)
    xpoints = list()
    ypoints = list()
    for dataset in dirs:
        date = dataset[0:10]
        date = pd.to_datetime(date)
        dataset_abs_path = os.path.join(datasets_path, dataset)
        num_lines = sum(1 for line in open(dataset_abs_path))
        num_lines = num_lines - 1
        xpoints.append(date)
        ypoints.append(num_lines)
    plt.xlabel("Date")
    plt.ylabel("Count of Open Ports")
    plt.margins(0.2)
    plt.plot(xpoints, ypoints, c='blue')
    plt.savefig("qotd_17.png")

plot(datasets_path)