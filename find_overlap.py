import pandas as pd

codes = pd.read_csv('<INSERT FILE DIRECTORY HERE>')
group1 = pd.DataFrame()
group2 = pd.DataFrame()
group1['Codes'] = codes['<Column1>']
group2['Codes'] = codes['<Column2>']
intersection = pd.merge(group1,group2)
intersection = intersection.dropna()
intersection = intersection.drop_duplicates()
intersection.to_csv('<INSERT FILE DIRECTORY HERE>',index = False, header = True)
