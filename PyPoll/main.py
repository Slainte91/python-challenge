#Your task is to create a Python script that analyzes the votes and calculates each of the following:
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.
import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

totalVotes = 0
candidates = []

with open(csvpath, "r", encoding='utf8', newline ='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader) 

for row in csvreader:
    totalVotes += 1

print (totalVotes)

