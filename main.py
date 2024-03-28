import csv, sys
import NeedlemanWunschAlgorithm as nwa

# Example of an input: C:/Users/Admin/Desktop/excel_prueba1.csv
input = input('Insert the file path: ')

with open(input, 'r') as file:
    # This makes sure that the lines are read as an csv file.
    csvFile = csv.reader(file)

    # This omits the first row on the csv document
    file.readline()

    for lines in csvFile:
        nwa.printOutput(lines)
file.close()
