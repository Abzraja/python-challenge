#import module for correcting file paths across different operating systems
import os

#import module that allows us to read csv files
import csv

#reference path to CSV data file
csvpath = os.path.join('.', 'Resources', 'election_data.csv')


#Read CSV file using the imported CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)


#set initial variables
    
    #total_vote_count to count the number of rows
    total_vote_count = 0
    candidate_votes_dict = {}
  # iterate through the rows
    for row in csvreader:
        
        #for each row add 1 to the total_vote_count to find total number of rows
        total_vote_count += 1
        
        #if value in csv candidate column is not in already in candidate_votes_dict dictionary 
        if row[2] not in candidate_votes_dict:
            
            #add the value to a dictionary as a key and give it a value of 0
            candidate_votes_dict[row[2]] = 0
        
        #if the value in candidate column is already a key in dictionary add +1 to it's value
        candidate_votes_dict[row[2]] += 1



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