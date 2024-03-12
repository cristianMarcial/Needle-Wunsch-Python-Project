import csv

print('Inserte \n')

try:
   input = input() #input = 'C:/Users/Admin/Desktop/excel_prueba1.csv'
except:
  print("An exception occurred")


with open(input, newline='') as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        print(lines)