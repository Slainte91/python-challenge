import os
import csv

csvpath = os.path.join("..","Resources", "budget_data.csv")

monthCounter = 0
greatestInc = 0
greatestDec = 0
averageChangeProfit = 0
netProfit = 0
greatestIncMonth = ""
greatestDecMonth = ""
lastProfit = 0
changeProfit = 0
recordedChanges = []
totalChanges = 0


with open(csvpath, "r", encoding='utf8', newline ='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader) 

for row in csvreader:
    monthCounter += 1
    currentProfit = row[1]
    netProfit += currentProfit
    changeProfit = currentProfit - lastProfit
    recordedChanges.append(changeProfit)

    if changeProfit > greatestInc:
        greatestInc = changeProfit
        greatestIncMonth = row[0]

    if changeProfit < greatestDec:
        greatestDec = changeProfit
        greatestDecMonth = row[0]

    lastProfit = currentProfit

for change in recordedChanges:
    totalChanges += change

averageChangeProfit = totalChanges/(monthCounter-1) 

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {monthCounter}")
print(f"Total: ${netProfit}")
print(f"Average Change: ${averageChangeProfit}")
print(f"Greatest Increase in Profits: {greatestIncMonth} (${greatestInc})")
print(f"Greatest Decrease in Profits: {greatestDecMonth} (${greatestDec})")