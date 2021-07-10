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
    #round the average
    avg = round(avg,2)

    #zip lists together
    zipped_list = zip(difference_list,month_list)
    
    #create dict out of zipped list (tuples)
    month_diff_dict = dict(zipped_list)

    #iterate through dictionary to find max_key_value and corresponding value
    for max_key_value in month_diff_dict:
        if max_key_value == max(month_diff_dict):
            #max_m = (month_diff_dict[max_key_value],max_key_value)
            max_month = (month_diff_dict[max_key_value])
            max_value = max_key_value

    #iterate through dictionary to find min_key_value and corresponding value
    for min_key_value in month_diff_dict:
        if min_key_value == min(month_diff_dict):
            min_month = (month_diff_dict[min_key_value])
            min_value = min_key_value

   #set a function for printing the report

def financial_analysis():
    
    return("Financial Analysis\n" + 
    "----------------------------\n" +
    f"Total Months: {row_count}\n" +
    f"Total $: {total_net_value}\n" +
    f"Average: {avg}\n" +
    f"Greatest Increase in Profits: {max_month} ($ {max_value})\n" +
    f"Greatest Decrease in Profits: {min_month} ($ {min_value})")
    
print(financial_analysis())
    
    #Specify the file to write to
text_file_path = os.path.join(".", "analysis", "financial_analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(text_file_path, 'w') as f:
    f.write(financial_analysis())
