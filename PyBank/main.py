#PyBank main.py

########Financial Analysis
########----------------------------
########Total Months: 25
########Total Revenue: $1241412
########Average Revenue Change: $216825
########Greatest Increase in Revenue: Sep-16 ($815531)
########Greatest Decrease in Revenue: Aug-12 ($-652794)

#Your task is to create a Python script that analyzes the records to calculate each of the following:




####The average change in revenue between months over the entire period

####The greatest increase in revenue (date and amount) over the entire period

####The greatest decrease in revenue (date and amount) over the entire period

####As an example, your analysis should look similar to the one below:





import os
import csv

budget_data_1 = os.path.join('budget_data_1.csv')
budget_data_2 = os.path.join('budget_data_2.csv')

####The total number of months included in the dataset
# -1 to account for header
months = 0-1

with open(budget_data_1, newline="") as csvfile:
	csvreader1 = csv.reader(csvfile, delimiter=",")
	for row in csvreader1:
		if row[1] != "":
			months = months + 1

with open(budget_data_2, newline="") as csvfile:
	csvreader1 = csv.reader(csvfile, delimiter=",")
	for row in csvreader1:
		if row[1] != "":
			months = months + 1

# -1 to account for header
months = months - 1
print(months)

# print("Total Months: " + str(months))

####The total amount of revenue gained over the entire period
revenue_list = []

with open(budget_data_1, newline="") as csvfile:
	csvreader1 = csv.reader(csvfile, delimiter=",")
	next (csvfile)
	for row in csvreader1:
		revenue_list.append(int(row[1]))
with open(budget_data_2, newline="") as csvfile:
	csvreader1 = csv.reader(csvfile, delimiter=",")
	next (csvfile)
	for row in csvreader1:
		revenue_list.append(int(row[1]))
total_revenue = sum(revenue_list)
# print(total_revenue)
# print(revenue_list)

change_list = []


for i in range (1, months):
	change = revenue_list[i] - revenue_list[i-1]
	change_list.append(change)

average_changes = sum(change_list)/(months-1)
# print (average_changes)

months_list = []
with open(budget_data_1, newline="") as csvfile:
	csvreader1 = csv.reader(csvfile, delimiter=",")
	next (csvfile)
	for row in csvreader1:
		months_list.append(row[0])
with open(budget_data_2, newline="") as csvfile:
	csvreader1 = csv.reader(csvfile, delimiter=",")
	next (csvfile)
	for row in csvreader1:
		months_list.append(row[0])

# print(months_list)


max_revenue = max(revenue_list)
min_revenue = min(revenue_list)

dictionary = dict(zip(months_list, revenue_list))

max_month = max(dictionary, key=dictionary.get)
min_month = min(dictionary, key=dictionary.get)

# print(max_month)
# print(min_month)

print('Total Months: ' + str(months))
print('Total Revenue: ' + "${:}".format(total_revenue))
print('Average Revenue Change: ' + str(average_changes))
print('Greatest Increase in Revenue: ' + max_month + ' (' + str("${:}".format(max_revenue)) + ')')
print('Greatest Decrease in Revenue: ' + min_month + ' (' + str("${:}".format(min_revenue)) + ')')








		