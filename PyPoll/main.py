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
    vote_count=0
    candidate_list = []

    #iterate through the rows
    for row in csvreader:
        vote_count += 1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])

#set a function for printing the report

def election_results():
    
    return ("Election Results\n" + 
        "-------------------------\n" +
        f"Total Votes: {vote_count}\n" +
        "-------------------------\n"
    )
    
    
print(election_results())

print(candidate_list)