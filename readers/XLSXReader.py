# This part needs more work
# Since xlsx format has no structure, you need more parameters,
# you want data from roes, or columns or what?
def xlsx_reader(path):
    import openpyxl
    xls_object = openpyxl.load_workbook(path)
    sheet_names = xls_object.get_sheet_names()
    sheet = xls_object.get_sheet_by_name(sheet_names[0])

    data = readData(sheet)
    attributes = generateAttributes(data[0])
    relation = "time_series"
    return {"attributes" : attributes, "data" : data, "relation" : relation}


def readData(sheet):
    data = []
    rowNr = 1
    while non_null(getRow(sheet, 'A', 'B', rowNr)):
        data.append(getRow(sheet, 'A', 'B', rowNr))
        rowNr += 1
    return data


def generateAttributes(exampleRow):
    attributes = []
    for index in range(0, len(exampleRow)):
        varName = "var_" + str(index).zfill(4)
        typeName = type(exampleRow[index]).__name__
        typeName = typeName.replace("float", "REAL") # float is not accepted by arff writer, it has to be REAL
        attributes.append((varName, typeName))
    return attributes


def getRow(sheet, startLetter, endLetter, rowNr):
    row = []
    for rowOfCellObjects in sheet[startLetter + `rowNr` : endLetter + `rowNr`]:
        for cellObj in rowOfCellObjects:
            row.append(cellObj.value)
    return row


def non_null(list):
    nones = 0
    for element in list:
        if element == None:
            nones += 1
    if nones == len(list):
        return False
    else:
        return True