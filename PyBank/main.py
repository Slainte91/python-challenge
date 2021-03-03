import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
#initialize variables
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
    #skip header row
    csvheader = next(csvreader) 

    for row in csvreader:
        #increment months by 1 each row
        monthCounter += 1
        #figure out our months current profit to compare to last month's
        currentProfit = int(row[1])
        #add to our total profit
        netProfit += currentProfit
        #calculate change and add to our list of recorded changes
        changeProfit = currentProfit - lastProfit
        recordedChanges.append(changeProfit)

        #set new variables if greater increase than previous
        if changeProfit > greatestInc:
            greatestInc = changeProfit
            greatestIncMonth = row[0]

        #set new variables if greater decrease than previous
        if changeProfit < greatestDec:
            greatestDec = changeProfit
            greatestDecMonth = row[0]

        #set current profit to last month to continue comparing
        lastProfit = currentProfit
#first index is not an actual change since it's where we started so remove it
recordedChanges.pop(0)

#calculate total changes
for change in recordedChanges:
    totalChanges += change

#average our changes
averageChangeProfit = round(totalChanges/(monthCounter-1),2) 

#print analysis to terminal
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {monthCounter}")
print(f"Total: ${netProfit}")
print(f"Average Change: ${averageChangeProfit}")
print(f"Greatest Increase in Profits: {greatestIncMonth} (${greatestInc})")
print(f"Greatest Decrease in Profits: {greatestDecMonth} (${greatestDec})")

#print analysis to txt file in analysis folder
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