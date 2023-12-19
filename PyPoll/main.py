# Modules
import os
import csv
 
# File to read
csvpath = os.path.join('Resources', 'election_data.csv')
 
# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader) # Skip the header row
 
# Variables
    total_votes = 0     # Counter for total number of votes
    candidates = []     # List to capture the names of candidates
    num_votes = []      # List to capture the number of votes each candidate received
    percent_votes = []  # List to capture the % of total votes each candidate received

 
# The total number of votes cast
    for row in csvreader:
        total_votes += 1

 
# Finding list of candidates & Number of votes received for each candidate
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1


# Calculate the percentage of votes received for each candidate
for votes in num_votes:
    percentage = (votes / total_votes) * 100
    percentage = round(percentage, 3)
    percent_votes.append(percentage)

# Finding the winning candidate
    winner = max(percent_votes)
    index = percent_votes.index(winner)
    winning_candidate = candidates[index]


# Print out results
print (f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {percent_votes[i]}% ({num_votes[i]})")
print(f"-------------------------")
print(f"Winner: {winning_candidate}")
print(f"-------------------------")


# Defining output to display for the .txt file
output = f'''
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{candidates[0]}: {percent_votes[0]}% ({num_votes[0]})
{candidates[1]}: {percent_votes[1]}% ({num_votes[1]})
{candidates[2]}: {percent_votes[2]}% ({num_votes[2]})
-------------------------
Winner: {winning_candidate}
-------------------------
'''

# Creating & Exporting results onto Election Results.txt file
csvpath = os.path.join('Analysis', 'Election Results.txt')
with open(csvpath,'w') as textfile:
    textfile.write(output)