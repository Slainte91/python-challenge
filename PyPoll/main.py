#Your task is to create a Python script that analyzes the votes and calculates each of the following:
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.
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
    votes.append(row(2))

    if row(2) in candidates:

    else:
        candidates.append(row(2))
print("Election Results")

print("-------------------------")
print (totalVotes)
print("-------------------------")
for candidate in candidates:
    candidateVotes = votes.count(candidate)
    percentVotes = candidateVotes/totalVotes

    if candidateVotes > greatestVotes:
        greatestVotes = candidateVotes
        greatestVotesName = candidate

    print(f"{candidate}: {percentVotes} ({candidateVotes})")

print("-------------------------")
print(f"Winner: {greatestVotesName}")
print("-------------------------")