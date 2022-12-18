# The data we need to retrieve
# 1. The total nbr of votes cast
# 2. List of candidates in the file
# 3. The percentage of votes for each candidate
# 4. Total nbr of votes by candidate
# 5. Winner of election based on popular vote

import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Create empty list to store candidate names in
candidate_options = []

# Create empty dictionary to store candidate names and corresponding total votes
candidate_votes = {}

# Winning Candidate and Winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read the header row and ignore it in the analysis
    headers = next(file_reader)

    for row in file_reader:
        # this means total_votes = total_votes + 1
        total_votes += 1

        # Candidate name is the 2nd index (or 3rd column header)
        candidate_name = row[2]

        # If the candidate doesn't match any existing candidates in the list we created above, then add it in
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count. This also creates each candidate as a key.
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        print(f"{candidate_name}: received {vote_percentage:.1f}% ({votes:,})\n")

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage: .1f}%\n"
        f"-----------------------\n")

    print(winning_candidate_summary)
