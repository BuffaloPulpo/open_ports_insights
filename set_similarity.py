import glob
import os
import pandas as pd

from helpers import get_jaccard_index

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)

datasets_path = r"C:\Users\Shuonan\Desktop\qotd_17"
dirs = os.listdir(datasets_path)

d_date_set = {}
for dataset in dirs:
    date = dataset[0:10]
    #date = pd.to_datetime(date)
    dataset_abs_path = os.path.join(datasets_path, dataset)
    df = pd.read_csv(dataset_abs_path)
    saddr_ips = set(df['saddr'].tolist())
    d_date_set[date] = saddr_ips

matrix_data = list()
list_date = list()
for each_date in d_date_set:
    list_index = list()
    set_self = d_date_set[each_date]
    for each in d_date_set:
        other_set = d_date_set[each]
        the_index = get_jaccard_index(set_self, other_set)
        the_index = round(the_index, 4)
        list_index.append(the_index)
    matrix_data.append(list_index)
    list_date.append(each_date)
    #print(list_index)

df = pd.DataFrame(matrix_data)
df.columns = list_date
df.rows = list_date
print(df)
df.to_csv("qotd_17.csv")