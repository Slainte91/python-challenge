import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

greatestVotes = 0
greatestVotesName = ""
percentVotes = 0
candidateVotes = 0
totalVotes = 0
candidates = []
votes = []

with open(csvpath, "r", encoding='utf8', newline ='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader) 

    for row in csvreader:
        totalVotes += 1
        votes.append(row[2])

        if row[2] not in candidates:
            candidates.append(row[2])

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
        candidateVotes = votes.count(candidate)
        percentVotes = round((candidateVotes/totalVotes)*100,3)

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