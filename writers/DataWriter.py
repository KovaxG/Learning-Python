from ARFFWriter import arff_writer

def write_data(data, fileName):
    file = open(fileName, 'w')
    file.write(arff_writer(data))
    file.close()