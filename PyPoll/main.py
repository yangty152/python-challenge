import os

import csv

file = os.path.join('..','PyPoll','Resources','election_data.csv')
print(file)
with open(file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    print(csv_header)
    VoterID = []
    County = []
    Candidate = []
    UniqueCandidate = []
    VoteCount = []
    VotePercent = []
    Winner = ""
    #i=0
    #a = 0
    #b = 0

    for row in csvreader:
        VoterID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])
    TotalVotesCast = len(VoterID)
    for i in range(len(Candidate)):
        if Candidate[i] not in UniqueCandidate:
            UniqueCandidate.append(Candidate[i])
        i+=1
    CountUniqueCandidate = len(UniqueCandidate)
    for b in range(CountUniqueCandidate):
        VoteCount.append(0)
        for a in range(len(Candidate)):
            if UniqueCandidate[b] == Candidate[a]:
                VoteCount[b] += 1
            else:
                VoteCount[b] = VoteCount[b]
            a+=1
        b+=1
    for i in VoteCount:
        VotePercent.append(i/TotalVotesCast)
    for i in range(len(VoteCount)):
        if VoteCount[i] == max(VoteCount):
            #print(VoteCount[i])
            #print(max(VoteCount))
            Winner = UniqueCandidate[i]
            #print(UniqueCandidate[i])
        else:
            Winner = Winner
        i+=1
 
    print("Election Results")
    print("-------------------------------")
    print(f"Total Votes: {TotalVotesCast}")
    print("-------------------------------")
    for i in range(len(VoteCount)):
        print(f"{UniqueCandidate[i]}: {VotePercent[i]} ({VoteCount[i]})")
        i+=1
    print("-------------------------------")
    print(f"Winner: {Winner}")
    print("-------------------------------")

