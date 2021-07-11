#import module for correcting file paths across different operating systems
import os

#import module that allows us to read csv files
import csv

#import statistics module and mean function - got from (https://www.guru99.com/find-average-list-python.html)
from statistics import mean

#reference path to CSV data file
csvpath = os.path.join('.', 'Resources', 'election_data.csv')


#Read CSV file using the imported CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)


#set initial variable
    
    #vote count = to number of rows in csv
    total_vote_count = 0
    khan_count = 0
    candidate_votes_dict = {}
  # iterate through the rows
    for row in csvreader:
        
        #for each row add 1 to the total_vote_count
        total_vote_count += 1
        
        #if value in csv candidate column is not in already in candidate_votes_dict dictionary 
        if row[2] not in candidate_votes_dict:
            
            #also add the value to a dictionary as a key and give it a value of 0
            candidate_votes_dict[row[2]] = 0
        
        #for each key in in vote_count dictionary add +1 to corresonpending key
        candidate_votes_dict[row[2]] += 1

    #candidate_percent = candidate_votes_dict["Khan"] / total_vote_count * 100
    #candidate_percent = round(candidate_percent,2)




#set a function for printing the report



#def candidate_results():
    
    for key, value in candidate_votes_dict.items() :
            candidate_percent = value / total_vote_count * 100
            candidate_percent = round(candidate_percent,2)
            candidate_percent = "{:.3f}".format(candidate_percent)
            print(f"{key}: {candidate_percent}% ({value})")


#find max value in dictionary and return corresponding key. the max value is the greatest number of votes, therefore the key is the winner
winner = max(candidate_votes_dict, key=candidate_votes_dict.get)

print(winner)

#print(candidate_results())


#def election_results():
    
 #   return ("Election Results\n" + 
  #      "-------------------------\n" +
   #     f"Total Votes: {total_vote_count}\n" +
    #    "-------------------------\n" +
    #candidate_results()
    #)
  
    
#print(election_results())