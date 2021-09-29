import json
from utils.JsonUtils import JsonUtils
import pandas as pd
from memory_profiler import profile


def df_generator(path: str):
    """
     usage: the df_generator can be used as follows.

        func = df_generator(path='../json_data/00.json')
        while True:
            try:
                df = next(func)
                print(df)
            except StopIteration as e:
                print(e.value)
                break
    """
    data = JsonUtils(path=path).read()
    for key, value in data.items():
        df = pd.DataFrame(value)
        yield df

