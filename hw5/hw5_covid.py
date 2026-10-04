# import needed modules
import requests
import json
import os
import csv
import calendar

# ---------------- Pull Data From csv File and Create Lists that Can Be Used ---------------- #

# create an empty dictionary and list
state_population = {}

# AI helped with code lines 14-21, I added comments and changed a couple names
with open("/home/ubuntu/data5510_mycode/hw5/states.csv", newline="") as file: # open the csv file and read it
    reader = csv.reader(file, delimiter="\t")

    # for each row in my file...
    for row in reader:

        # the first column will be a key in my dictionary and the next will be the population associated with that key
        state_population[row[0]] = int(row[1])


# check to make sure dictionary is showing correct information
# print(state_population)

# establish variables to keep track of state with highest and lowest overall percent population
max_percent_pop = 0
min_percent_pop = 100
max_state = ''
min_state = ''
max_month = ''
min_month = ''
max_year = ''
min_year = ''
max_cases = 0
min_cases = 0
max_pop = 0
min_pop = 0

# loop through dictionary and for each state...
for state in state_population:

    # ------------------- Get URL, Set Up Parameters, Request Data, and Load Into JSON ------------------- #

    # URL to pull data
    DATASET_ID = "pwn4-m3yp"
    BASE_URL = f"https://data.cdc.gov/resource/{DATASET_ID}.json"
    # print(BASE_URL) # check to make sure URL is correct


    # establish parameters for what data we are wanting to pull
    params = {
        "$where": f"state='{state}' AND end_date >= '2020-01-01' AND end_date <= '2023-12-31'",
        "$order": "end_date ASC"
    }

    # use the requests class to produce the object req that uses the parameters established
    req = requests.get(BASE_URL, params=params)
    # print(req.text)

    # convert json into a dictionary
    dct = json.loads(req.text)

    # ------------------- Find Needed Keys for First Two Statisticts, Pull Specific Data, and Perform Analyze ------------------- #

    # establish starting variable 
    end_date_key = "end_date"
    new_cases_key = "new_cases"
    new_cases = []

    max_new_cases = 0
    max_new_date = ''

    total = 0
    count = 0

    # loop through dictionary
    for d in dct:

        # each time, append the number of new cases to a list 
        new_cases.append(float(d[new_cases_key]))

        # keep track the max number of cases and date by comparing to previous max
        if float(d[new_cases_key]) > float(max_new_cases):
            max_new_cases = d[new_cases_key]
            max_new_date = d[end_date_key]

    # loop through the list just created
    for cases in new_cases:
        total += cases # keep track of total number of new cases
        count += 1 # keep track of number of weeks

    # calculate the average number of new weekly cases
    average = total / count

    # split the date and time and only return the date
    date_only = max_new_date.split("T")[0]

    # -------------------- Find Month and Year, with the highest new number of covid cases -------------------- #

    # create a dictionary to store year and month along with total new cases
    monthly_totals = {}

    # loop through dictionary
    for date in dct:

        # pull out year and month from each end date
        # print(date[end_date_key][0:7]) # making sure I got the year and month
        year_month = date[end_date_key][0:7]

        # if a new year and month is not in the dictionary...
        if year_month not in monthly_totals:

            # create a key in the monthly_totals dictionary and set the value equal to 0
            monthly_totals[year_month] = 0

        # Each time a month and year matches one of the keys, add the new cases value to that key
        monthly_totals[year_month] += float(date[new_cases_key])

    # check to see if all of the monthly totals were put in the right keys
    # print(monthly_totals)

    # establish variable to keep track of the max monthly total of new cases
    monthly_max = 0
    month_max = ''

    # loop through the dictionary and for each month...
    for month in monthly_totals:

        # if the monthly total is greater than the current monthly total found...
        if monthly_totals[month] > monthly_max:

            # replace the monthly total max to keep track of the highest
            monthly_max = monthly_totals[month]
            # also replace the month that has the highest number of new cases
            month_max = month

    # check to see if printing correct maxes
    # print(month_max, monthly_max)

    # next two lines imported from AI. This code is used to report the month and year with month name and then the year
    year, month = month_max.split("-")
    month_name = calendar.month_name[int(month)]

    # ------------------------- Finding % of Population and Keep Track of State with Highest and Lowest------------------------- #

    # find the percent of the population by diving the monthly max by the population of the state and multiplying by 100
    percent_pop = (float(monthly_max)/float(state_population[state])) * 100
    # round answer to include only 2 digits after the decimal place
    percent_pop_round = round(percent_pop, 2) 

    # if the percent of population for this state is greater than the current highest percent of population...
    if percent_pop_round > max_percent_pop:

        # keep track of the new highest percent of population variables
        max_percent_pop = percent_pop_round
        max_state = state
        max_month = month_name
        max_year = year
        max_cases = monthly_max
        max_pop = state_population[state]

    # if the percent of population for this state is less than the current lowest percent of population...
    if percent_pop_round < min_percent_pop:

        # keep track of the new highest percent of population variables
        min_percent_pop = percent_pop_round
        min_state = state
        min_month = month_name
        min_year = year
        min_cases = monthly_max
        min_pop = state_population[state]

    # ---------------------------------- Display Findings --------------------------------- #

    print()
    print(f"State Name: {state}")
    print()
    print(f"Average number of new weekly cases for the entire state dataset: {round(average, 2)}")
    print(f"Week with the highest new number of covid cases: {date_only} ({int(float(max_new_cases))})")
    print(f"Month and Year, with the highest new number of covid cases: {month_name} {year} ({monthly_max})")
    print(f"Month and Year, with highest new number, percentage of population: {percent_pop_round}% (Population: {state_population[state]})") 
    print()
    print("------------------------------------------------------------------")
    print()

    # saving dictionaries in a json file
    curr_dir = os.path.dirname(__file__) # get current directory
    json.dump(dct, open(curr_dir + "/data/" + state + ".json", "w"))

# --------------------------------- Display Final Summary --------------------------------- #

print("==================== SUMMARY ACROSS ALL STATES ====================")
print("State with HIGHEST percentage of population during its highest month: ")
print(f"{max_state} - {max_percent_pop}% in {max_month} {max_year} ({max_cases} cases; Population: {max_pop})")
print()
print("State with LOWEST percentage of population during its highest month: ")
print(f"{min_state} - {min_percent_pop}% in {min_month} {min_year} ({min_cases} cases; Population: {min_pop})")
print()