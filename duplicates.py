import pandas as pd

codes = pd.read_csv('<INSERT FILE DIRECTORY HERE>')
code_duplicate = codes['<COLUMN NAME>']
duplicate_data = codes[code_duplicate.duplicated(keep = False)]
duplicate_data_other = codes[code_duplicate.duplicated(keep = 'first')]

useful_data = duplicate_data[['<COLUMN NAME>', '<COLUMN NAME>', '<COLUMN NAME>', '<COLUMN NAME>']]
print(useful_data)
print('There are ' + str(len(duplicate_data_other)) + ' duplicates' )


useful_data.to_csv('<INSERT FILE DIRECTORY HERE>')
