import csv

data1 = []
data2 = []

with open('dataset_1.csv','r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
            data1.append(row)

with open('dataset_2_sorted.csv','r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
            data2.append(row)

header1 = data1[0]
planet_data1 = data1[1:]
header2 = data2[0]
planet_data2 = data2[1:]

headers = header1 + header2
planet_data = []
for index,data_row in enumerate(planet_data1):
        planet_data.append(planet_data1[index] + planet_data2[index])

with open('final1.csv','a+') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)
