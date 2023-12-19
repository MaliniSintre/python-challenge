# Modules
import os
import csv

# Specify the file to read
csvpath = os.path.join('Resources', 'budget_data.csv')

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader) # Skip the header row

# Variables
    total_months = 0
    net_total = 0
    previous_profit_loss = 0
    changes = []
    months =[]

# Calculate total number of months included in the dataset
# And net total amount of "Profit/Losses"
    for row in csvreader:
        total_months += 1
        net_total += int(row[1])

# Calculate the changes in "Profit/Losses" over the entire period,
# And then the average of those changes
        change_PL = int(row[1]) - previous_profit_loss
        changes.append(change_PL)
        months.append(row[0])
        previous_profit_loss = int(row[1])

    Ave_change = round(sum(changes[1:]) / (total_months -1),2)

# The greatest increase in profits (date and amount) over the entire period
greatest_increase = max(changes)
greatest_increase_month = months[changes.index(greatest_increase)]

# The greatest decrease in profits (date and amount) over the entire period
greatest_decrease = min(changes)
greatest_decrease_month = months[changes.index(greatest_decrease)]


# Print out results
print (f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${Ave_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")


# Defining output to display for the .txt file
output = f'''
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${Ave_change}
Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})
'''

# Creating & Exporting results onto Financial_Analysis.txt file
csvpath = os.path.join('Analysis', 'Financial_Analysis.txt')
with open(csvpath,'w') as textfile:
    textfile.write(output)