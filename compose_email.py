import pandas as pd

email_list = pd.read_csv('<INSERT FILE DIRECTORY HERE>')
#read .csv file into dataframe
emails = pd.DataFrame()
#initialize empty data frame
email_bodies = []
#initialize empty list to hold the bodies of emails
for i in email_list['{Column that holds list of names}']:
    email_text = "Dear " + i + ", {body of email here}"
    email_bodies.append(email_text)
#goes through list of names and adds each name to the body of the email.
emails['names'] = email_list['{Column that holds list of names}']
emails['email_addresses'] = email_list['{Column that holds list of emails}']
emails['email_bodies'] = email_bodies
emails.to_csv('<INSERT FILE DIRECTORY HERE>', index = False, header = True)
