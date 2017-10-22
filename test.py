from readers.DataReader import read_data
from writers.DataWriter import write_data

arff_data = read_data("synth_multidim_010_000.arff")
xlsx_data = read_data("RandomData.xlsx")

print("XLSX Data -----------------------")

print(xlsx_data["attributes"])
print(xlsx_data["data"])
print(xlsx_data["relation"])
print()

print("ARFF Data -----------------------")
print(arff_data["attributes"])
print(arff_data["data"])
print(arff_data["relation"])
print()

print(write_data(xlsx_data))
