import pandas as pd
import numpy as np

def data_frame(arff_data):
    data = arff_data["data"]

    x = []
    y = []
    for row in data:
        x.append(row[0])
        y.append(row[1])

    df = pd.DataFrame(y, index=x, columns=["value"])
    print(df)