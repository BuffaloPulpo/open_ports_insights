import re

regex_port_number = r'(\d+)(?!.*\d)'
regex_date = r'(\d{4}-\d{2}-\d{2})'


def get_port_number_from_filepath(file_path):
    match_port = (re.search(regex_port_number, file_path)).group()
    return match_port


def get_date_from_filepath(file_path):
    match_date = (re.search(regex_date, file_path)).group()
    return match_date


def get_protocol_type_from_filepath(file_path):
    hi_protocol = 'TBA'
    if 'tcp' in file_path:
        hi_protocol = 'TCP'
    if 'udp' in file_path:
        hi_protocol = 'UDP'
    return hi_protocol


def get_jaccard_index(set1, set2):
    intersected_ips = set1.intersection(set2)
    union_ips = set1.union(set2)
    the_index = len(intersected_ips) / len(union_ips)
    return the_index
