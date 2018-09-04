import csv
from collections import Counter
import os

with open('election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    header = next(csvreader)

    votesCounted = Counter()
    candidateList = []
    percentage = []
    answer = []

    for row in csvreader:
        candidateList.append(row[2])

    totalVotes = len(candidateList)

    for name in candidateList:
        votesCounted[name] += 1

    winner = max(zip(votesCounted.keys()))
    names = tuple(votesCounted.keys())
    votes = tuple(votesCounted.values())

    for value in votes:
        percentage.append((int(value)/totalVotes)*100)

    answer.append('Election Results')
    answer.append('-----------------------')
    answer.append('Total Votes: ' + str(totalVotes))
    answer.append('-----------------------')

    for x in range(len(names)):
        answer.append(names[x] + ': ' + str(round(percentage[x],1)) + '% ' + '(' + str(votes[x]) + ')')
    answer.append('-----------------------')
    answer.append('Winner: ' + winner[0])
    answer.append('-----------------------')
    print("\n".join((answer)))






