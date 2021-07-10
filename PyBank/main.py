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
    
    #set initial variables
    row_count=0
    total_net_value=0
    difference_list = []
    month_list = []
    previous_value = 0

    #iterate through the rows
    for row in csvreader:
        row_count += 1
        total_net_value = total_net_value + int(row[1])

        #read value from current row and subtract from previous value and append into list
        difference_list.append(int(row[1]) - previous_value)
        
        #read value from current row into month_list
        month_list.append(row[0])
        
        #set the value in current row as previous_value for next row
        previous_value = int (row[1])


    #drop first value in list as first value had nothing to subtract from and will negatively influence our mean
    difference_list.pop(0)
    month_list.pop(0)
    #use mean function from statistics module to get mean of list and store in avg variable
    avg = mean(difference_list)

    #zip lists together
    #zipped_list = lambda: zip(month_list,difference_list) - would not iterate through 2 iterations when placed after each other. had to use lambda to overcome this.
    zipped_list = zip(difference_list,month_list)
    #create dict out of zipped list (tuples)
    dict = dict(zipped_list)

    print(dict)



    #iterate through dictionary
    #max_value = [x for x in dict in (zipped_list) if max(difference_list)]
    #print(max_value)
    
    #find max row in difference list
    #x = [x for x in zipped_list() if max(difference_list) in x][0]

    #find min row in difference list    
    #y = [y for y in zipped_list() if min(difference_list) in y][0]
    

    
    print(f"Total Months: {row_count}")
    print(f"Total $: {total_net_value}")
    print(f"Change list: {difference_list}")
    print(f"Average: {avg}")
    #print(f"Greatest Increase in Profits: {x[0]} {x[1]}")
    #print(f"Greatest Decrease in Profits: {y[0]} {y[1]}")
    
    

