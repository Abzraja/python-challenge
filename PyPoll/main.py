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

#print output to terminal



def election_results_report_header():
    return(f"Election Results\n" +
        "-------------------------\n" +
        f"Total Votes: {total_vote_count}\n" +
        "-------------------------")

def candidate_results():
    results_list = []
    #iterate through each key (candidate) in candidate_vote dictionary
    for key, value in candidate_votes_dict.items():
        #calculate the vote percentage for each key(candidate) by taking the value of the key and dividing by total_vote_count
        candidate_percent = value / total_vote_count * 100
            #round the candidate_percent value to 2 decimal places
        candidate_percent = round(candidate_percent,2)
        #show 3 figures after decimal as in the example on GitLab
        candidate_percent = "{:.3f}".format(candidate_percent)
        #for each key save the key, candidate_percent and value into a list
        results_list.append(f"{key}: {candidate_percent}% ({value})")
    #return each item in the list on a new line        
    return("\n".join(results_list))
    
    
    
def election_results_winner():
        #find max value in dictionary and return corresponding key. the max value is the greatest number of votes, therefore the key is the winner
        winner = max(candidate_votes_dict, key=candidate_votes_dict.get)
        return("-------------------------\n" +
        f"Winner: {winner}\n"
        "-------------------------")


#output to text file

#Specify the file to write to
text_file_path = os.path.join(".", "analysis", "election_results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(text_file_path, 'w') as f:
    f.write(election_results_report_header())
    f.write("\n")
    f.write(candidate_results())
    f.write("\n")
    f.write(election_results_winner())




#print to terminal - the header which contains the total vote count
print(election_results_report_header())
#print to terminal - the candidate_results function which contains separated list of each candidate's results
print(candidate_results())
#print to terminal - the winner function which contains the winner
print(election_results_winner())


