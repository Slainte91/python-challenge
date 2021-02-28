import os
import csv

csvpath = os.path.join('..', 'Resources', 'PyBank_budget_data.csv')

monthCounter = 0
greatestInc = 0
greatestDec = 0
averageProfit = 0
netProfit = 0

with open(csvpath, "r", encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader) # pop one row

for row in csvreader:
    monthCounter += 1
    currentProfit = row[1]
    netprofit += currentProfit

    if currentProfit > greatestInc:
        greatestInc = currentProfit

    if currentProfit < greatestDec:
        greatestDec = currentProfit

    


