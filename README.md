# **Python-Challenge**
## Summary
An extremely difficult task that took me nearly 20 hours of racking my brain and looking for solutions. Did not expect this assignment to be so difficult but I ran into issues at many stages. I think the Python week should have been 2 weeks with the second week having multiple exercises to help us understand things we can do easily with python and get our head around the syntax.


## Before you begin checklist
- [x] Create a new repository for this project called python-challenge. Do not add this homework to an existing repository.
- [x] Clone the new repository to your computer.
- [x] Inside your local git repository, create a directory for each Python Challenge. Use folder names corresponding to the challenges: PyBank and  PyPoll.
      Inside of each folder that you just created, add the following:
- [x] A new file called main.py. This will be the main script to run for each analysis.
- [x] A "Resources" folder that contains the CSV files you used. Make sure your script has the correct path to the CSV file.
- [x] An "analysis" folder that contains your text file that has the results from your analysis.
- [x] Push the above changes to GitHub or GitLab.


## PyBank
![PyBank Image](https://s17026.pcdn.co/wp-content/uploads/sites/9/2018/08/Business-bank-account-e1534519443766.jpeg)

## Checklist
Your task is to create a Python script that analyzes the records to calculate each of the following:
- [x] The total number of months included in the dataset
- [x] The net total amount of "Profit/Losses" over the entire period
- [x] Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
- [x] The greatest increase in profits (date and amount) over the entire period
- [x] The greatest decrease in profits (date and amount) over the entire period
- [x] As an example, your analysis should look similar to the one below:
- [x] In addition, your final script should both print the analysis to the terminal and export a text file with the results.


### Issues
* Took me a while to figure out I had to create a dictionary from a zipped list of 2 lists.
* Had trouble iterating through the dictionary to find and return the values I wanted. I first wrote out the for loop with the long method, then I figured out how to condense it to one line.
* I initially printed the report to the terminal but could not put this into the text file. Had to define a function to return the report values and then then use that function to printo to terminal and also wrote the function the text file.




## PyPoll
![PyPoll Image](https://images-na.ssl-images-amazon.com/images/I/51cOM2ZPaoL.png)

## Checklist
Your task is to create a Python script that analyzes the votes and calculates each of the following:
- [x] The total number of votes cast
- [x] A complete list of candidates who received votes
- [x] The percentage of votes each candidate won
- [x] The total number of votes each candidate won
- [x] The winner of the election based on popular vote.
- [x] As an example, your analysis should look similar to the one below:
- [x] n addition, your final script should both print the analysis to the terminal and export a text file with the results.

### Issues
* Had an issue right at the start with this one. I blame the Gitlab instructions saying to create a complete "**list**" of candidates. I had to create a dictionary instead.
* Took me hours of trying iterate the dictionary to get the values I wanted. In the end I realised each time a unique candidate was found in the csv to create a dictionary with that candidate as a key and to give it a value of 0, then if the value in the candidate column is not unique to + 1 to its value for it's key. Really took forever to figure this out and I need practice with it badly.
* after this I had an issue of how to print the results to the file. I had ot use a function but function would only return the first item in the loop and stop on the return straight away.
* Got around this by appending the loop items to a list, then I returned the list instead
* this gave another issue with all list items being on one line.
* then i had to google out and figure out how to split them onto one line each.
* This whole assignment took way longer than it should have. 

##Conclusion
While I believe I have aced the assignment it took a lot of hard work and I think even though I managed to figure it out, it took much longer than it should have. I am still not comfortable with loops and nested loops in python or list an dictionary comprehensions when it comes to loops.

Phew! all done.
