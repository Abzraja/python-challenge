#import module for correcting file paths across different operating systems
import os

#import module that allows us to read csv files
import csv

#reference path to CSV data file
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')


#Read CSV file using the imported CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    row_count=0
    total_net_value=0

    for row in csvreader:
        row_count += 1
        total_net_value = total_net_value + int(row[1])
        
        #read current row value from profit/loss column
        current_value = int(row[1])
        #read next line value as intger (I got this code from - https://docs.python.org/3/library/csv.html)
        next_value = int(next(csvreader)[1])

        #add next line value from current line value and store in change variable
        change = current_value + next_value


    print(f"Total Months: {row_count}")
    print(f"Total $: {total_net_value}")
    print(f"Current Value: {current_value}")
    print(f"Next Value: {next_value}")
    print(f"Change: {change}")
    

