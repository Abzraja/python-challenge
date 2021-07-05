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
    net_value=0

    for row in csvreader:
        row_count += 1
        net_value = net_value + int(row[1])
    
    print(f"Total Months: {row_count}")
    print(f"Total $: {net_value}")
    

