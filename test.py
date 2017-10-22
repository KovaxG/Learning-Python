from readers.DataReader import read_data

file_names = ["data\\synth_multidim_010_000.arff",
              "data\\RandomData.xlsx",
              "data\\example.arff"]

# Reading from files
for fileName in file_names:
    data = read_data(fileName)

    print("---" + fileName + "---")
    print(data["attributes"])
    print(data["data"])
    print(data["relation"])
    print()

# Writing to files
from writers.DataWriter import write_data
excel_data = read_data("data\\RandomData.xlsx")
write_data(excel_data, "data\\example.arff")

# Displaying data
from display.SimplePlot import simple_plot
from display.DataFrameDisplay import data_frame

simple_plot(excel_data)
data_frame(excel_data)

