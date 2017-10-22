from ARFFReader import arff_reader
from XLSXReader import xlsx_reader


def read_data(path):
    reader = {"arff" : arff_reader,
              "xlsx" : xlsx_reader}

    extension = path.split(".").pop()
    return reader[extension](path)
