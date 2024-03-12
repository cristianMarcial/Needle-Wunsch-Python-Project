import csv
import NeedlemanWunschAlgorithm as nwa

try:
    input = input('Insert the file path: ') #input = 'C:/Users/Admin/Desktop/excel_prueba1.csv'

    with open(input, newline='') as file:
        #This makes sure that the lines are read as an csv file.
        csvFile = csv.reader(file)

        #This omits the first line on the doc, which has ...
        file.readline()
        
        for lines in csvFile:
            nwa.printOutput(lines[1])
    file.close()

except:
    print("An exception occurred while opening the file. Recompile this program again and make sure the input is well written")