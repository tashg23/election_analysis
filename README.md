# election_analysis

## Project Overview 
Colorado Board of Elections requires: 
- Total nbr of votes cast
- Complete list of candidates who received votes 
- Total nbr of votes each candidate received 
- Percentage of votes each candidate won
- Winner of election by popular vote 
- County with highest voter turnout 
- Nbr of votes by county and percentage

## Resources 
- Data source: election_results.csv
- Software: Python 3.10.4 

## Election-Audit Results 
- There were 369,711 votes cast in this congressional election
  - Jefferson: 38, 855 votes (10.5%)
  - Denver: 306, 055 votes (6.7%)
  - Arapahoe: 24, 801 votes (6.7%) 
- Denver had the highest voter turnout 
  - Charles Stockham: 85, 213 votes (23%) 
  - Diana DeGette: 272, 892 votes (73.8%) 
  - Raymon Doane: 11, 606 votes (3.1%) 
- Diana DeGette won the Colorado election with a total of 272, 892 votes which was 73.8% of all votes. 

## Summary 
This script can be reused for future elections, with minor tweaks. We would have to change the file names and path and potentially the locations of the county name and candidate name columns depending on the structure of any future data files. We would also have to change the name of the output text file. Additionally, depending on the cleanliness of future data files, we may have to add some cleansing steps. 
