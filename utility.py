
from pandas import DataFrame


def file_write(file_path, content):
    f = open(file_path, "a")
    for c in content:
        f.write(c)
    f.close()


def load_lookup(lookup_path: str):
    lookup_dict = {}
    lookup_data = open(lookup_path,"r")
    for line in lookup_data:
        data = line.split("|")
        lookup_dict[data[0]] = data[1]
    return lookup_dict

def load_splay(splay_path: str):
    splay_dict = {}
    splay_data = open(splay_path,"r")
    for line in splay_data:
        data = line.split("|")
        splay_dict[data[1]] = data[0]
    return splay_dict

def load_test_data(input_path: str):
    input_list = []
    input_data = open(input_path,"r")
    for line in input_data:
        input_list.append(line)
    return input_list

def df_to_file(lookup_path: str, splay_path: str, df_text: DataFrame):
    f = open(splay_path, "a")
    f2 = open(lookup_path, "a")
    for index, row in df_text.iterrows():
        splay_text = "{}|{}\n".format(index, row['text'])
        lookup_text = "{}|{}\n".format(index, row['Link'])
        f.write(splay_text)
        f2.write(lookup_text)
    f.close()
    f2.close()

