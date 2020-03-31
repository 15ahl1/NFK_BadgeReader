import csv
def writeCSV(tableList):
    writer = csv.writer(open("out.csv", 'w'))
    for line in tableList:
        writer.writerow(line)




writeCSV([['name', 'address', 'phone', 'etc'],
         ['bob', '2 main st', '703', 'yada'],
         ['bob', '2 main st', '703', 'yada']])
