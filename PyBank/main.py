import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

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
currentProfit = 0


with open(csvpath, "r", encoding='utf8', newline ='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader) 

    for row in csvreader:
        monthCounter += 1
        currentProfit = int(row[1])
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

recordedChanges.pop(0)

for change in recordedChanges:
    totalChanges += change

averageChangeProfit = round(totalChanges/(monthCounter-1),2) 

print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {monthCounter}")
print(f"Total: ${netProfit}")
print(f"Average Change: ${averageChangeProfit}")
print(f"Greatest Increase in Profits: {greatestIncMonth} (${greatestInc})")
print(f"Greatest Decrease in Profits: {greatestDecMonth} (${greatestDec})")

output = os.path.join("analysis", "analysis.txt")
with open(output, "w", newline = "", encoding = "utf8") as txtfile:
    # used https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file/36571602
    print("Financial Analysis", file = txtfile)
    print("-------------------------", file = txtfile)
    print(f"Total Months: {monthCounter}", file = txtfile)
    print(f"Total: ${netProfit}", file = txtfile)
    print(f"Average Change: ${averageChangeProfit}", file = txtfile)
    print(f"Greatest Increase in Profits: {greatestIncMonth} (${greatestInc})", file = txtfile)
    print(f"Greatest Decrease in Profits: {greatestDecMonth} (${greatestDec})", file = txtfile)