import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

#initialize our variables
greatestVotes = 0
greatestVotesName = ""
percentVotes = 0
candidateVotes = 0
totalVotes = 0
candidates = []
votes = []

with open(csvpath, "r", encoding='utf8', newline ='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip the header
    csvheader = next(csvreader) 

    for row in csvreader:
        #increment by one our total votes for each vote cast
        totalVotes += 1
        #add the name of those votes to our list so we may count it later
        votes.append(row[2])

        #get a list of each candidate's name once
        if row[2] not in candidates:
            candidates.append(row[2])

#print our analysis to both the terminal and a text file
output = os.path.join("analysis", "analysis.txt")
with open(output, "w", newline = "", encoding = "utf8") as txtfile:
    # used https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file/36571602
    print("Election Results")
    print("Election Results", file=txtfile)
    print("-------------------------")
    print("-------------------------", file=txtfile)
    print(f"Total Votes: {totalVotes}")
    print(f"Total Votes: {totalVotes}", file=txtfile)
    print("-------------------------")
    print("-------------------------", file=txtfile)

    for candidate in candidates:
        #count our votes using count method I found here https://www.w3schools.com/python/python_lists_methods.asp
        candidateVotes = votes.count(candidate)
        #calculate percent of votes gotten and round to 3 decimal places using round which
        #I found here https://www.w3schools.com/python/ref_func_round.asp
        percentVotes = round((candidateVotes/totalVotes)*100,3)
        
        #check if candidate has received more votes than previous ones to name the winner
        if candidateVotes > greatestVotes:
            greatestVotes = candidateVotes
            greatestVotesName = candidate

        print(f"{candidate}: {percentVotes}% ({candidateVotes})")
        print(f"{candidate}: {percentVotes}% ({candidateVotes})", file=txtfile)

    print("-------------------------")
    print("-------------------------", file=txtfile)
    print(f"Winner: {greatestVotesName}")
    print(f"Winner: {greatestVotesName}", file=txtfile)
    print("-------------------------")
    print("-------------------------", file=txtfile)