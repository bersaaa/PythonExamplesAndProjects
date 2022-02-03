import csv
from telnetlib import XDISPLOC
import numpy as np
import pandas as pd

csv_file = pd.read_csv(r"NBA_season1718_salary.csv")
salaries = csv_file.iloc[:,].values
# Read the dataset
print(salaries,'\n')

# Read the first 10 data
print(csv_file.iloc[:10,].values , '\n')

# Find out how many data there are
print(len(salaries),'\n')

# Find the average of all salaries
mean_df = csv_file['season17_18'].mean()
print(mean_df,'\n')

# Find the highest salary
max_df = csv_file['season17_18'].max()
print(max_df,'\n')

# Find the last name of the highest paid basketball player.
fullName = csv_file[csv_file.isin([int(max_df)]).any(axis=1)].iloc[0].values
name, surname = str(fullName[1]).split(' ')
print(surname,'\n')

# Find the team of a basketball player named Kevin Durant
i = csv_file[csv_file['Player'] == 'Kevin Durant']['Tm']
print(i)
print('\n')

fullTeam = csv_file['Tm'].tolist()
teams = list(dict.fromkeys(list(fullTeam)))
team= [str(x) for x in teams]
team = [x for x in team if x != 'nan']
print(team)
print('\n')

# Find average salaries by grouping basketball players by team
for i in team:
    buffer=i
    members = csv_file.groupby('Tm')
    member = members.get_group(buffer)
    print(member)
    print(len(member))
    print(member['season17_18'].mean())
    print('\n')
    
# Find how many different teams are in the data set
print(len(team))
print('\n')

# Find out how many players are in which team #
length=[]  
for i in csv_file['Player']:
    length.append(len(str(i)))
    
# Find the length of the names of the players and add them as a new column to the dataset  #
csv_file['Length']=length
print(csv_file)
print('\n')

# List the basketball players whose salary is 15000000 and whose team is SAS #
people=members.get_group('SAS')
person = [x for x in people['season17_18'] if x == 15000000]
print(person)
print('\n')

# Delete the team names from the dataset. #
csv_file.drop('Tm', 1, inplace=True)
print(csv_file)
print('\n')



