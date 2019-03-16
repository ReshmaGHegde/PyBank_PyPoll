import os
import csv

#define the required lists

Candidate_Name = []
Candidate_County = []
Candidate_VoterID = []
dict_polls={}
dict_summary = {}

#pull the columns into lists
election_data_path = os.path.join("Resources", "election_data.csv")
with open(election_data_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csv_reader:
        Candidate_VoterID.append(row[0])
        Candidate_County.append(row[1])
        Candidate_Name.append(row[2])
        
#calculating the total votes
total = len(Candidate_VoterID)
print(f'Election Results')
print(f'-------------------------')
print("Total Votes: ",total)
print(f'-------------------------')


with open(election_data_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csv_reader:
        key=row[2]
        if key not in dict_polls:
         # insert name_key into dictionary and initialize to 0
            dict_polls[key]=0
         # count the name key inside dictionary
        dict_polls[key]+=1

# Compute the percentages of each name key of dict_polls and insert into dict_summary
   
    #print(dict_polls)
    for name in dict_polls:
        dict_summary[name]=round((dict_polls[name]/total)*100)
          
        # Output to console
        print(str(name)+": "+str(dict_summary[name])+"% "+"("+str(dict_polls[name])+")")

      
    # Find larget value of the key/value pair inside dictionary and place the key name inside winner
        highest = 0
        for name in dict_summary:
            if highest < dict_summary[name]:
               highest = dict_summary[name]
               winner = name

#obtaining the winner info
print(f'---------------------------')
print(f'Winner : {winner}')
print(f'---------------------------')


            