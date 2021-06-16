import pandas as pd
#we will be using the pandas package for this
dates = pd.read_csv('<INSERT .CSV FILE PATH HERE>', converters = {'Date': lambda x: str(x)})
#reads .csv file and puts values into pandas dataframe; reads values in 'Date' column as string instead of int
dates['Date'] = dates['Date'].apply(lambda x: x.zfill(8))
#fills in leading zeros into the dates if the number of characters in a value is less than 8
new_date = []
#initialize empty list new_date to append reformatted dates to
for i in dates['Date']:
    month = i[0:2]
    #month is the 1st and 2nd characters in i
    day = i[2:4]
    #day is the 3rd and 4th characters in i
    year = i[4:8]
    #year is the last 4 characters in i
    newdate = day+month+year
    #newdate takes the string variables day, month year and combines them to get DDMMYYYY date format
    new_date.append(newdate)
    #appends valued of newdate to empty new_date list

#for loop iterates through every value in the dates['Date'] column and uses string indexing to switch from MMDDYYY format to DDMMYYYY format
dates['New_date'] = new_date
#create new column 'New_date' in dates dataframe where we add the values of the new_date list to the column
dates.to_csv('<INSERT .CSV FILE PATH HERE>', index = False, header = True)
#save updated dataframe as .csv file
