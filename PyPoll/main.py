#PyPoll main.py
#The total number of votes cast 

#TO DO: DO IT FOR ALL CANDIDATES


import os
import csv

election_data_1 = os.path.join('election_data_1.csv')
election_data_2 = os.path.join('election_data_2.csv')

vote_count = 0

#read csv1
with open(election_data_1, newline="") as csvfile:
	csvreader1 = csv.reader(csvfile, delimiter=",")
	for row in csvreader1:
		if row[1] != "":
			vote_count = vote_count + 1
		pass

#take out the count of the headers
vote_count = vote_count - 1

#read csv2
with open(election_data_2, newline="") as csvfile:
	csvreader2 = csv.reader(csvfile, delimiter=",")
	for row in csvreader2:
		if row[1] != "":
			vote_count = vote_count + 1
		pass

#take out the count of the headers
vote_count = vote_count - 1
print("Vote Count: " + str(vote_count))

#A complete list of candidates who received votes (PROBABLY BY CREATING A LIST)
candidates = []
with open(election_data_1, newline="") as csvfile:
	csvreader1 = csv.reader(csvfile, delimiter=",")
	next(csvfile)
	for row in csvreader1:
		if row[2] not in candidates:
			candidate = row[2]
			candidates.append(candidate)
		pass

with open(election_data_2, newline="") as csvfile:
	csvreader2 = csv.reader(csvfile, delimiter=",")
	next(csvfile)
	for row in csvreader2:
		if row[2] not in candidates:
			candidate = row[2]
			candidates.append(candidate)
		pass
print("Candidates: " + str(candidates))
print("                               ")

#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

num_candidates = len(candidates)
#print(num_candidates)
votes = []

for x in range(0,num_candidates):
	votes.append(0)

#print(votes)

final_count = dict(zip(candidates, votes))

#print(final_count)

#candidate_votes = 0
#vote_count_list = []
winner_votes = 0

with open(election_data_1, newline="") as csvfile3:
	csvreader3 = csv.reader(csvfile3, delimiter=",")
	next(csvfile3)
	for row in csvreader3:
		key = row[2]
		#value = elem[0] for elem in final_count.get(key)
		final_count[key] = final_count[key] + 1
		#final_count[key] = value
		#if final_count > winner_votes:
			#winner_votes = final_count
			#winner = row[2]

with open(election_data_2, newline="") as csvfile3:
	csvreader3 = csv.reader(csvfile3, delimiter=",")
	next(csvfile3)
	for row in csvreader3:
		key = row[2]
		final_count[key] = final_count[key] + 1


#print(final_count)

for key, value in final_count.items():
    percent_of_vote = value/vote_count
    final_count[key] = [value, "{:.1%}".format(percent_of_vote)]

print(final_count)

#print ("{:.1%}".format(percent_of_vote)

winner = max(final_count, key=final_count.get)
#print(winner)

	# for person in candidates:
	# 	for row in csvreader3:
	# 		if row[2] == person:
	# 			candidate_votes = candidate_votes + 1
	# 		#if person != candidates[0]:
	# 			#print(row)
	# 		#for row in csvreader1:
 #            	#if row[2] == person:
 #                #candidate_votes = candidate_votes + 1
	# 	#vote_count_list.append(candidate_votes)
	# 	if candidate_votes > winner_votes:
	# 		winner = person

	# 	print("Candidate name: " + person)
	# 	print("Total votes: " + str(candidate_votes))
	# 	percent_of_vote = candidate_votes/vote_count
	# 	print ("{:.1%}".format(percent_of_vote))
	# 	print("                               ")
	# 	candidate_votes = 0
print("The winner is " + winner + "!")

