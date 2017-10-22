import arff

def arff_reader(path):
    return arff.load(open(path, "rb"))
