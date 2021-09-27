from utils.JsonUtils import JsonUtils
import os
import pandas as pd
import random
from typing import List, Dict


class DataConcat(object):
    def __init__(self, table_value: List[List]):
        self.table_value = table_value
        self.delimiter = random.choice('#$@-=|;:,')

    def contact(self):
        print(self.table_value)
        contact_value = []
        sample_value = [random.choice(self.table_value) for i in range(random.randint(1, 9))]
        for i in range(random.randint(1, 20)):
            a_contact_value = self.delimiter.join([''.join(sample_value[i]) for i in range(len(sample_value))])
            contact_value.append(a_contact_value)
        return contact_value


def contact_data_from_file(base_path: str):
    all_files = os.listdir(base_path)
    data_dict = dict()
    for file in all_files:
        data = JsonUtils(path=base_path + file).read()
        for key, value in data.items():
            contact_table_value = DataConcat(value).contact()
            print(contact_table_value)
            data_dict[key] = contact_table_value
    JsonUtils(base_path + file.split('.')[0] + 'contact''.json').write(data_dict)


if __name__ == '__main__':
    contact_data_from_file('../json_data/')
