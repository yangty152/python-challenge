# Modules
import os
import csv

# Open election_data.csv
file = os.path.join('..','PyPoll','Resources','election_data.csv')
with open(file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    
    #Define variables
    VoterID = []
    Candidate = []
    UniqueCandidate = []
    VoteCount = []
    VotePercent = []
    Winner = ""

    #Populate VoterID and Candidate list
    for row in csvreader:
        VoterID.append(row[0])
        Candidate.append(row[2])
    
    #Caculate total Votes
    TotalVotesCast = len(VoterID)
    
    #Find unique candidate by looping through Candidate list and place the unique candidate to a new list
    for i in range(len(Candidate)):
        if Candidate[i] not in UniqueCandidate:
            UniqueCandidate.append(Candidate[i])
        i+=1
    
    #Count total votes for each unique Candidate
    for i in range(len(UniqueCandidate)):
        VoteCount.append(0)
        for j in range(len(Candidate)):
            if UniqueCandidate[i] == Candidate[j]:
                VoteCount[i] += 1
            else:
                VoteCount[i] = VoteCount[i]
            j+=1
        i+=1
    
    #Calculate %
    for i in VoteCount:
        VotePercent.append(i/TotalVotesCast)
    
    #Find the winner
    for i in range(len(VoteCount)):
        if VoteCount[i] == max(VoteCount):
            Winner = UniqueCandidate[i]
        else:
            Winner = Winner
        i+=1
 
    #Output the result
    print("Election Results")
    print("-------------------------------")
    print(f"Total Votes: {TotalVotesCast}")
    print("-------------------------------")
    for i in range(len(VoteCount)):
        VotePercent[i] = "{:.3%}".format(VotePercent[i])
        print(f'{UniqueCandidate[i]}: {VotePercent[i]} ({VoteCount[i]})')
        i+=1
    print("-------------------------------")
    print(f"Winner: {Winner}")
    print("-------------------------------")


# Write output to a text file
output_path = os.path.join("..", "PyPoll","output", "PyPollResult.txt")

with open(output_path, 'w', newline='') as outputfile:

    outputfile.write(f"Election Results"'\n')
    outputfile.write(f"-------------------------------"'\n')
    outputfile.write(f"Total Votes: {TotalVotesCast}"'\n')
    outputfile.write(f"-------------------------------"'\n')
    for i in range(len(VoteCount)):
        outputfile.write(f'{UniqueCandidate[i]}: {VotePercent[i]} ({VoteCount[i]})''\n')
        i+=1
    outputfile.write(f"-------------------------------"'\n')
    outputfile.write(f"Winner: {Winner}"'\n')
    outputfile.write(f"-------------------------------"'\n')
    outputfile.close
   