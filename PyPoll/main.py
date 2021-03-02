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

print("Election Results")
print("-------------------------")
print (f"Total Votes: {totalVotes}")
print("-------------------------")

for candidate in candidates:
    candidateVotes = votes.count(candidate)
    percentVotes = round((candidateVotes/totalVotes)*100,3)

    if candidateVotes > greatestVotes:
        greatestVotes = candidateVotes
        greatestVotesName = candidate

    print(f"{candidate}: {percentVotes}% ({candidateVotes})")

print("-------------------------")
print(f"Winner: {greatestVotesName}")
print("-------------------------")