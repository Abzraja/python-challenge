#import module for correcting file paths across different operating systems
import os

#import module that allows us to read csv files
import csv

#import statistics module and mean function - got from (https://www.guru99.com/find-average-list-python.html)
from statistics import mean

#reference path to CSV data file
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')


#Read CSV file using the imported CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    row_count=0
    total_net_value=0
    change_list = []
    change = 0

    for row in csvreader:
        row_count += 1
        total_net_value = total_net_value + int(row[1])
        
        change = int(row[1]) - change
        change_list.append(change)
        change = int (row[1])
         
        #read current row value from profit/loss column
        #current_value = int(row[1])
        #read next line value as intger (I got this code from - https://docs.python.org/3/library/csv.html)
        #next_value = int(next(csvreader)[1])

        #add next line value from current line value and store in change variable
        #change.append(current_value + next_value)

    #drop first value in list as not a change
    change_list.pop(0)
    avg = mean(change_list)
    
    
    print(f"Total Months: {row_count}")
    print(f"Total $: {total_net_value}")
    #print(f"Current Value: {current_value}")
    #print(f"Next Value: {next_value}")
    print(f"Change list: {change_list}")
    print(f"Average: {avg}")
    

